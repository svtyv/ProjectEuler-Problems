def primeFactor():  # function for finding primes greater than 2
    n = 2
    counter = 0
    primes = []
    numbers = []
    while n < 10000:  # maximum value of the prime to be found
        if not n % 2 == 0 and not n % 3 == 0:
            numbers.append(n)
        n += 1
    for element in numbers:
        for integer in numbers:
            if integer >= element:  # optimization. No need to run denominators greater than numerators
                break
            if element % integer == 0 and element != integer:  # if divisible, move on to the next integer
                break
            else:
                counter += 1  # counts the times integer is not divisible
        if numbers.index(
                element) == counter:  # if index == counter, number was not divisible with any integer and is prime
            primes.append(element)
        counter = 0
    return primes


def Factors(ListOfPrimes: list):
    AreDivisible = []
    for integer in ListOfPrimes:
        if 600851475143 % integer == 0:  # checks if integer in list is a factor of the number
            AreDivisible.append(integer)
    print(AreDivisible)


Factors(primeFactor())
