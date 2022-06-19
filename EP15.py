def lattice():
    small_set = []
    another_set = []
    highest_value = 0
    n = 1
    a = 0
    k = 1
    while n < 22:
        small_set.append(n)
        n += 1
    while k <= 10:
        for i in small_set:
            a = a + i
            another_set.append(a)
        a = another_set[0]
        small_set.clear()
        small_set.append(1)
        for b in another_set[1:]:
            a = b + a
            small_set.append(a)
        highest_value = max(another_set)
        another_set = []
        a = 0
        k += 1

    print(small_set)
    print(highest_value)


lattice()
