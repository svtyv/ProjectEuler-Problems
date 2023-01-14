def main():
    a = sum_of_corners(1001)
    print(a + 1)
    # started with 3x3 and add the first (1) in the end


def sum_of_corners(side_length: int) -> int:
    summed = 0
    for i in range(3, side_length + 1, 2):
        square = i ** 2
        third = square - i + 1
        second = third - i + 1
        first = second - i + 1
        summed += (first + second + third + square)
    return summed


if __name__ == "__main__":
    main()
