import sys

import scripts.objs as o
import scripts.measure as m

if len(sys.argv) < 2:
    print("Не указан сценарий нагрузки")
    sys.exit(1)

N = 1

AXUM_HOST = "http://localhost:6789"
ACTIX_HOST = "http://localhost:9876"

ROUTES = ["/flat", "/mixed", "/deep"]
PAYLOADS = [
    o.generate_flat_obj(),
    o.generate_mixed_obj(),
    o.generate_deep_obj(),
]

DEGRADATION_SCENARIO = [i for i in range(1000, 10000, 1000)] + [i for i in range(10000, 50001, 10000)]
MAX_LOAD_SCENARIO = [9000 for _ in range(0, 15)]

DEGRADATION_DIR = "degradation"
MAX_LOAD_DIR = "max_load"

arg = sys.argv[1]
if arg == "d":
    axum_measures = m.measures_server(
        AXUM_HOST,
        DEGRADATION_SCENARIO,
        ROUTES,
        PAYLOADS,
        N,
    )
elif arg == "c":
    pass
else:
    print("incorrect arg")
    sys.exit(1)
