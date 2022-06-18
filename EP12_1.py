def triangular_numbers():
    numbers = []
    for i in range(12200, 12400):
        triangle = int(i * (i + 1) / 2)
        if triangle % 2 == 0 and triangle % 3 ==0 and triangle%5 ==0:
            numbers.append(triangle)
    # numbers.sort(reverse=True)
    divisibilities = []
    a = 0
    for i in numbers:
        n = i
        while n >= 1:
            if i % n == 0:
                a += 1
            n -= 1
        divisibilities.append(a)
        a = 0
    print(divisibilities)
    print(divisibilities.index(max(divisibilities)) + 1, max(divisibilities))
    print(len(numbers))
    print(numbers)


triangular_numbers()
