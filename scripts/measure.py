import pandas as pd

import loader as l
import container_manager as c

def measure_server(
    shost: str,
    users_cnts: list[int],
    route: str,
    payload: dict,
    n: int = 100
) -> pd.DataFrame:
    c.docker_start()
    measures = []

    for i in range(1, n + 1):
        result = l.load_scenario_route(shost, route, users_cnts, payload)
        measures.append(result)
        if i != n:
            c.docker_restart()
    c.docker_down()

    dfs = [pd.DataFrame(r) for r in measures]

    combined = pd.concat(dfs).groupby("id", as_index=False).mean(numeric_only=True)
    combined = combined.drop('id', axis=1)
    
    print(combined)
    return combined

def measures_server(
    shost: str,
    users_cnts: list[int],
    routes: list[str],
    payloads: list[dict],
    n: int = 100
) -> list[pd.DataFrame]:
    measures = []
    for (i, route) in enumerate(routes):
        measures.append(measure_server(
            shost,
            users_cnts,
            route,
            payload=payloads[i],
            n=n
        ))
    return measures
