# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

# primeFactor from EP3

def primeFactor():  # function for finding primes greater than 2
    n = 2
    counter = 0
    primes = []
    numbers = []
    while n < 110000:  # maximum value of the prime to be found
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


primes = primeFactor()
print(primes[9998])
print(len(primes))
