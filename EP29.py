def main():
    sequence = {}

    for i in range(2, 101):
        for j in range(2, 101):
            sequence[i ** j] = 1
    print(len(sequence))


if __name__ == '__main__':
    main()
