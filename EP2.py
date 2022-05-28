def fibonakki():
    n = 1
    last = 1
    theSum: int = 0
    while n <= 4000000:
        if n % 2 == 0:
            theSum += n
        n = n + last
        last = n - last
    print(theSum)
fibonakki()
