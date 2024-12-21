MEAN_ARRIVAL_TIME = 2  # Tempo medio di arrivo dei job [secondo/job]

EDGE_SERVERS = 2
CLOUD_SERVERS = 2

P_C = 0.8

SEED = 123456789

REPLICATIONS = 10

INFINITE = 0
FINITE = 1
SIMULATION_TYPE = FINITE

BETTER = 0
STANDARD = 1
SCALABILITY = 2
BETTER_SCALABILITY = 3
MODEL = BETTER_SCALABILITY

START = 0.0  # initial time
STOP = 86400.00  # terminal (close the door) time
STOP_INFINITE = float('inf')
INFINITY = float('inf')  # must be much larger than STOP

ALPHA = 0.05 # 95% confidence

K = 260
B = 1096