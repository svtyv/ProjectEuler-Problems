import math


def primes(max: int):
    a = int(math.sqrt(max))
    list_of_primes_helper = [1, 2, 3]
    for b in range(list_of_primes_helper[-1] + 1, a + 1):
        for prime in list_of_primes_helper[1:]:
            if b % prime == 0:
                break
            if prime == list_of_primes_helper[-1] and b % prime != 0:
                list_of_primes_helper.append(b)
                break
            if b % prime != 0:
                continue

    list_of_primes = []
    for i in list_of_primes_helper[:]:
        list_of_primes.append(i)

    for i in range(list_of_primes_helper[-1] + 1, max + 1):
        for b in list_of_primes_helper[1:]:
            if i % b == 0:
                break
            if b == list_of_primes_helper[-1] and i % b != 0:
                list_of_primes.append(i)
            if i % b != 0:
                continue

    return list_of_primes


def amicable():
    primes_off = primes(10000)
    possibly_amicable = []
    raw_list = []
    sums = 0
    sums1 = 0
    for i in range(2, 10001):
        if i in primes_off:
            continue
        raw_list.append(i)
    for i in raw_list[:]:
        for a in range(1, int(i // 2) + 1):
            if i % a == 0:
                sums += a
        if sums in raw_list[:] and sums != i:
            for b in range(1, (sums // 2) + 1):
                if sums % b == 0:
                    sums1 += b
            if sums1 == i:
                possibly_amicable.append([i, sums])
                raw_list.remove(sums1)

        sums = 0
        sums1 = 0
    amicable_sum = 0
    for i in possibly_amicable:
        amicable_sum += sum(i)
    return amicable_sum


print(amicable())
