from primes import primes
import numpy as np
import time

primes = primes(2, 10000)
primes_dict = {}
primes_list = list(map(int, primes))
for prime in primes_list:
    primes_dict[prime] = 1
composites = [x for x in range(9, 10000) if x % 2 != 0 and x not in primes_dict]
start = time.time()
calculating = True
while calculating:
    for comp in composites:
        for a in range(1, int(comp / 2)):
            x = comp - int(2 * (a ** 2))
            if x in primes_dict:
                break
            elif x <= 0:
                print(comp)
                calculating = False
