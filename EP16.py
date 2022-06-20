def sum_of_digits(number: int):
    number = str(number)
    list = []
    for char in number:
        if char != 0:
            list.append(int(char))
    answer = sum(list)
    print(answer)


sum_of_digits(2 ** 1000)
