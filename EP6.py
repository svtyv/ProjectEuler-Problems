#Square of the sums solved on paper (n(n+1)/2)^2
def sumOfSquares():
    squares = []
    n = 1
    while n < 101:
        a = n ** 2
        squares.append(a)
        n += 1
    squaresSummed = sum(squares)
    result = 25502500 - squaresSummed
    return result


print(sumOfSquares())
