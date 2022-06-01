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
