def palindrome():
    palindromes = []
    a = 999
    b = 999
    while a > 99:
        while b > 99:
            ab = int(a * b)
            ab = str(ab)
            if ab == ab[::-1]:
                ab = int(ab)
                palindromes.append(ab)
            b -= 1
        b = 999
        a -= 1
    palindromes.sort(key=None,reverse=True)
    print(palindromes)


palindrome()
