import simpy
import random
import statistics

RANDOM_SEED = 42
ARRIVAL_RATE = 10     # ПБД за годину
SERVICE_RATE = 12     # обробка ПБД за годину
SIM_TIME = 6          # години

wait_times = []

def pbd_process(env, officer):
    arrival_time = env.now
    with officer.request() as request:
        yield request
        wait_times.append(env.now - arrival_time)
        service_time = random.expovariate(SERVICE_RATE)
        yield env.timeout(service_time)

def arrival_generator(env, officer):
    while True:
        yield env.timeout(random.expovariate(ARRIVAL_RATE))
        env.process(pbd_process(env, officer))

random.seed(RANDOM_SEED)
env = simpy.Environment()
officer = simpy.Resource(env, capacity=1)

env.process(arrival_generator(env, officer))
env.run(until=SIM_TIME)

print(f"Середній час очікування ПБД: {statistics.mean(wait_times):.2f} год")
print(f"Максимальний час очікування: {max(wait_times):.2f} год")
