import requests
import statistics
from datetime import datetime

from locust import HttpUser, task, between
from locust.env import Environment
from locust.stats import stats_printer, stats_history

import gevent
from gevent import monkey

monkey.patch_all()

def load_route(
    shost: str, 
    route: str, 
    users_cnt: int, 
    payload: dict = None, 
    run_time: int = 10,
    metrics_route: str = "/metrics",
    metrics_interval: int = 2
) -> dict:
    print(f"start for {users_cnt} users")
    class User(HttpUser):
        wait_time = between(0.1, 0.3)
        host = shost

        @task
        def hit_endpoint(self):
            self.client.post(route, json=payload or {})

    env = Environment(user_classes=[User])
    env.create_local_runner()

    gevent.spawn(stats_printer(env.stats))
    gevent.spawn(stats_history, env.runner)

    metrics_data = []

    def collect_metrics():
        metrics_url = f"{shost.rstrip('/')}{metrics_route}"
        while True:
            try:
                r = requests.get(metrics_url, timeout=3)
                if r.ok:
                    data = r.json()
                    data["timestamp"] = datetime.isoformat(data['timestamp'])
                    metrics_data.append(data)
                    print(f"metrics: CPU={data['cpu_percent']:.1f}% RAM={data['ram_percent']:.1f}% Threads={data['thread_count']}")
                else:
                    print(f"Ошибка при получении метрик: {r.status_code}")
            except Exception as e:
                print(f"Ошибка запроса метрик: {e}")
            gevent.sleep(metrics_interval)

    gevent.spawn(collect_metrics)

    env.runner.start(user_count=users_cnt, spawn_rate=users_cnt)

    gevent.sleep(run_time)

    env.runner.quit()

    print("\n=== Результаты ===")
    for stat in env.stats.entries.values():
        print(f"{stat.name}: {stat.num_requests} запросов, "
              f"{stat.avg_response_time:.2f} мс, "
              f"{stat.fail_ratio*100:.2f}% ошибок")

    cpu_values = [m["cpu_percent"] for m in metrics_data]
    ram_values = [m["ram_percent"] for m in metrics_data]

    return {
        'users_cnt': users_cnt,
        'num_requests': env.stats.total.num_requests,
        'avg_response_time': env.stats.total.avg_response_time,
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
    
    return metrics


# import objs as o
# if __name__ == "__main__":
#     h = o.generate_flat_obj()
#     o.print_obj(h)
#     users = [i for i in range(10000, 100001, 10000)]
#     for user in users:
#         load_route(
#             shost="http://localhost:6789",
#             route="/flat",
#             users_cnt=user,
#             payload=o.generate_flat_obj(),
#             run_time=10
#         )
