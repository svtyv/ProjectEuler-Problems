import math


# Lowest has to be divisible by 2
def prime_finder(lowest: int, highest: int):
    base = math.floor(math.sqrt(highest))
    base_primes = []
    the_numbers = []
    rolling_number = 3
    for b in range(lowest, base):
        base_primes.append(b)
    for k in base_primes[::-1]:
        for a in base_primes[:]:
            if a >= k:
                break
            if k % a == 0:
                base_primes.remove(k)
                break
    while rolling_number < highest:
        for prime in base_primes:
            if not math.gcd(rolling_number, prime) == 1:
                break
            elif prime == base_primes[-1]:
                the_numbers.append(rolling_number)
        rolling_number += 2
    the_sum = sum(base_primes) + sum(the_numbers)

    return the_sum


print(prime_finder(2, 2000000))
