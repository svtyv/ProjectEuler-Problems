#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

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
    palindromes.sort(key=None, reverse=True)
    print(palindromes)


palindrome()
