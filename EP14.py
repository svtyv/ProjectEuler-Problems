def collatz():
    n = 999999
    terms = [0]
    cnt = 1
    startin_number = 0
    while n > 1000:
        if n % 2 != 0:
            b = n
            while True:
                b = b * 3 + 1
                cnt += 1
                if b % 2 == 0:
                    while True:
                        b = b / 2
                        cnt += 1
                        if b == 1:
                            if cnt > terms[0]:
                                terms.insert(terms.index(max(terms)), cnt)
                                startin_number = n
                            break
                        if b % 2 != 0:
                            break
                if b == 1:
                    break
        n -= 1
        cnt = 1

    print(startin_number, max(terms))


collatz()
