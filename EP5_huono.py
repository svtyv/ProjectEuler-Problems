# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def multiple():
    n = 1
    theNumber = []
    while n < 999999999:
        if n % 20 == 0:
            if n % 19 == 0:
                if n % 18 == 0:
                    if n % 17 == 0:
                        if n % 16 == 0:
                            if n % 15 == 0:
                                if n % 14 == 0:
                                    if n % 13 == 0:
                                        if n % 12 == 0:
                                            if n % 11 == 0:
                                                theNumber.append(n)
        n += 1
    return theNumber


print(multiple())
