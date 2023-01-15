def main():
    separated_numbers = []
    sums_of_powers = []
    summed_power = 0
    for i in range(2, 1000000):
        for j in str(i):
            separated_numbers.append(int(j))
        for k in separated_numbers:
            summed_power += k ** 5
        if summed_power == i:
            sums_of_powers.append(i)
        separated_numbers.clear()
        summed_power = 0
    print(sum(sums_of_powers))


if __name__ == '__main__':
    main()
