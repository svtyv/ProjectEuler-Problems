from prime import prime_machine

primes = prime_machine.primes


def main():
    d = term_b(1000)
    lenthgs = {}

    for i in d:
        for j in range(-200, -1):  # tested in batches of 200, longest series of primes is 71 by -61 and 971

            length_quads = len(quadratic(j, i))

            lenthgs[length_quads] = (j, i)

    print(max(lenthgs.keys()))
    print(lenthgs.keys())
    print(lenthgs)


def term_b(b: int):
    b_in_primes = primes(b)
    b_values = []
    for i in b_in_primes:
        b_values.append(i)
        b_values.append(i * -1)
    b_values.append(-1)
    b_values.append(1)
    b_values = sorted(b_values)

    return b_values


def quadratic(a: int, b: int):
    n = 0
    list_of_solutions = []

    while True:
        q = (n ** 2) + (a * n) + b
        if q in primes(q + 1):
            list_of_solutions.append(q)
            n += 1
        else:
            break

    return list_of_solutions


if __name__ == '__main__':
    print(main())
