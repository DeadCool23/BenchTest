#!/bin/python3

import os
import sys

import objs as o
import loader as l
import measure as m
from dirs import MEASURES_DIR, MAX_LOAD_DIR, DEGRADATION_DIR

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Не указан сценарий нагрузки")
        sys.exit(1)

N = 100

__FRAMEWORK_NAMES = [
    "axum", 
    "actix"
]
DOCKER_SERVICES = [
    "axum-server",
    "actix-server"
]
AXUM_HOST = "http://localhost:6789"
ACTIX_HOST = "http://localhost:9876"
SHOSTS = [
    AXUM_HOST,
    ACTIX_HOST,
]

ROUTES = [
    "/flat", 
    "/mixed", 
    "/deep",
]
PAYLOADS = [
    o.generate_flat_obj(),
    o.generate_mixed_obj(),
    o.generate_deep_obj(),
]

DEGRADATION_SCENARIO = [i for i in range(1000, 10000, 1000)] + [i for i in range(10000, 50001, 10000)]
MAX_LOAD_SCENARIO = [10000 for _ in range(0, 15)]

def save_scenario_measures(scenario_dir: str, scenario: list[int]):
    for (name, docker_service, shost) in zip(__FRAMEWORK_NAMES, DOCKER_SERVICES, SHOSTS):
        print(f"=======TESTING {name}=======")
        for (route, payload) in zip(ROUTES, PAYLOADS):
            filename = f"{name}_{route.lstrip('/')}.csv"
            filepath = os.path.join(scenario_dir, filename)

            l.CONTAINER_NAME = docker_service
            if os.path.exists(filepath):
                print(f"Метрики {route} для фреймворка {name} уже собраны")
                continue
            mes = m.measure_server(
                shost,
                scenario,
                route,
                payload,
                N,
            )
            
            mes.to_csv(filepath, index=False)
            print(f"Saved: {filepath}")

if __name__ == '__main__':
    save_ddir = os.path.join(MEASURES_DIR, DEGRADATION_DIR)
    save_mdir = os.path.join(MEASURES_DIR, MAX_LOAD_DIR)

    os.makedirs(save_ddir, exist_ok=True)
    os.makedirs(save_mdir, exist_ok=True)

    arg = sys.argv[1]
    if arg == "d":
        save_scenario_measures(save_ddir, DEGRADATION_SCENARIO)
    elif arg == "m":
        save_scenario_measures(save_mdir, MAX_LOAD_SCENARIO)
    else:
        print("incorrect arg")
        sys.exit(1)
