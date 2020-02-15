import random
import time

def estimate_pi(n):
    num_point_circle = 0
    num_point_total = 0
    global pi
    for i in range(n):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        distance = x**2 + y**2
        if distance <= 1:
            num_point_circle += 1
        num_point_total += 1
        i += 1
    pi = 4*num_point_circle/num_point_total
    return pi
def select_iterations():
    global n
    n = int(input('enter the number of iterartion steps: '))
    return n
select_iterations()
print('you chose ',n,' steps.')
start = time.perf_counter()
estimate_pi(n)
print('for ',n,' iteration steps, pi has an estimated value of ',pi)
end = time.perf_counter()
duration = end - start
print('the duration of the estimation took ',duration,'seconds')



