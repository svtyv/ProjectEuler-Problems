def main():
    print(fib_1000())


def fib_1000():
    f2 = 1
    fib = 2
    a = 4
    b = 5
    fibonaccis = {}
    while len(str(fib)) and len(str(f2)) < 1000:
        f2 = f2 + fib
        fibonaccis[f2] = a
        fib = f2 + fib
        fibonaccis[fib] = b
        a += 2
        b += 2

    return fibonaccis[fib] and fibonaccis[f2]


if __name__ == '__main__':
    main()
