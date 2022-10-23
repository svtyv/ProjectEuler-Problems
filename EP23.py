import math


def main(max: int):
    abundants_to_be_checked = abundant(max)

    sums_of_abundants = summing_abundants(abundants_to_be_checked)
    sum_of_not_abundants = 0

    for i in range(1, max + 1):
        if i in sums_of_abundants:
            continue
        sum_of_not_abundants += i
    print(sum_of_not_abundants)


def summing_abundants(numbers: list):
    sums = {}
    for i in numbers:
        for j in numbers:
            sums[i + j] = 1
    return sums


def factors(number: int) -> list:
    a = 1
    factors = []
    while a <= number // 2:
        if number % a == 0:
            factors.append(a)
        a += 1
    return factors


def abundant(max: int) -> list:
    a = 2
    abundant_numbers = []
    list_of_primes = primes(max)
    while a <= max:
        if a in list_of_primes:
            a += 1
            continue
        sum_of_factors = sum(factors(a))
        if sum_of_factors > a:
            abundant_numbers.append(a)
        a += 1
    return abundant_numbers


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


if __name__ == '__main__':
    main(28123)
