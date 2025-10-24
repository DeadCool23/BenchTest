import docker
import requests
import statistics

from locust import HttpUser, task, between
from locust.env import Environment

import gevent
import gevent.monkey
gevent.monkey.patch_all()

EPS=0.1
CONTAINER_NAME="helloworld"

SID=0

def load_route(
    shost: str, 
    route: str, 
    users_cnt: int, 
    payload: dict = None, 
    run_time: int = 10,
    metrics_route: str = "/metrics",
    metrics_interval: int = 2
) -> dict:
    global SID
    print(f"start for {users_cnt} users")
    class User(HttpUser):
        wait_time = between(0.1, 0.3)
        host = shost

        @task
        def hit_endpoint(self):
            self.client.post(route, json=payload or {})

    env = Environment(user_classes=[User])
    env.create_local_runner()

    metrics_data = []

    def collect_metrics():
        metrics_url = f"{shost.rstrip('/')}{metrics_route}"
        while True:
            try:
                r = requests.get(metrics_url, timeout=3)
                if r.ok:
                    data = r.json()
                    metrics_data.append(data)
                    print(f"metrics: CPU={data['cpu_percent']:.1f}% RAM={data['ram_percent']:.1f}% Threads={data['thread_count']}")
                else:
                    print(f"Ошибка при получении метрик: {r.status_code}")
            except Exception as e:
                print(f"Ошибка запроса метрик: {e}")
            gevent.sleep(metrics_interval)
    
    def collect_docker_metrics():
        client = docker.from_env()

        container = client.containers.get(CONTAINER_NAME)

        while True:
            stats = container.stats(stream=False)

            cpu_delta = stats["cpu_stats"]["cpu_usage"]["total_usage"] - stats["precpu_stats"]["cpu_usage"]["total_usage"]
            system_delta = stats["cpu_stats"]["system_cpu_usage"] - stats["precpu_stats"]["system_cpu_usage"]

            cpu_percent = 0.0
            if system_delta > 0 and cpu_delta > 0:
                online_cpus = stats["cpu_stats"].get("online_cpus", 1)
                cpu_percent = (cpu_delta / system_delta) * online_cpus * 100.0

            mem_usage = stats["memory_stats"]["usage"]
            mem_limit = stats["memory_stats"]["limit"]
            mem_percent = (mem_usage / mem_limit) * 100.0

            if mem_percent > EPS and cpu_percent > EPS:
                metrics_data.append({
                    "cpu_percent": cpu_percent,
                    "ram_percent": mem_percent
                })
                print(f"CPU={cpu_percent:.1f}%  RAM={mem_percent:.1f}% ({mem_usage/1024/1024:.1f}MB/{mem_limit/1024/1024:.1f}MB)")

            gevent.sleep(metrics_interval)

    gevent.spawn(collect_docker_metrics)

    env.runner.start(user_count=users_cnt, spawn_rate=users_cnt)

    gevent.sleep(run_time)

    env.runner.quit()

    print("\n=== Результаты ===")
    for stat in env.stats.entries.values():
        print(f"{stat.name}: {stat.num_requests} запросов, "
              f"{stat.avg_response_time:.2f} мс, "
              f"{stat.fail_ratio*100:.2f}% ошибок\n\n")

    cpu_values = [m["cpu_percent"] for m in metrics_data]
    ram_values = [m["ram_percent"] for m in metrics_data]

    SID += 1
    return {
        'id': SID - 1,

        'users_cnt': users_cnt,
        'num_requests': env.stats.total.num_requests,

        'response_time': env.stats.total.avg_response_time,
        
        'min_cpu_percent': min(cpu_values), 
        'med_cpu_percent': statistics.median(cpu_values),
        'max_cpu_percent': max(cpu_values),

        'min_ram_percent': min(ram_values),
        'med_ram_percent': statistics.median(ram_values),
        'max_ram_percent': max(ram_values),
    }

def load_scenario_route(
    shost: str, 
    route: str, 
    users_cnts: list[int], 
    payload: dict = None, 
    run_time: int = 10,
    metrics_route: str = "/metrics",
    metrics_interval: int = 2
) -> list[dict]:
    global SID
    metrics = []

    for users_cnt in users_cnts:
        metrics.append(load_route(
            shost,
            route,
            users_cnt,
            payload,
            run_time,
            metrics_route,
            metrics_interval
        ))
    
    SID = 0
    return metrics
