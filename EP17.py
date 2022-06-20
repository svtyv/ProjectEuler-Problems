def letters(start: int, stop: int):
    hundred = len("hundred")
    tens = {1: len("ten"), 2: len("twenty"), 3: len("thirty"), 4: len("forty"), 5: len("fifty"), 6: len("sixty"),
            7: len("seventy"),
            8: len("eighty"), 9: len("ninety")}

    one_digits = {1: len("one"), 2: len("two"), 3: len("three"), 4: len("four"), 5: len("five"), 6: len("six"),
                  7: len("seven"),
                  8: len("eight"), 9: len("nine")}
    teens = {11: len("eleven"), 12: len("twelve"), 13: len("thirteen"), 14: len("fourteen"), 15: len("fifteen"),
             16: len("sixteen"), 17: len("seventeen"), 18: len("eighteen"), 19: len("nineteen")}
    list_of_numbers = []
    sum_of_letters = 0
    for i in range(start, stop + 1):
        list_of_numbers.append(i)
    for integer in list_of_numbers:
        if integer == 1000:
            sum_of_letters = sum_of_letters + 11
            break
        if len(str(integer)) < 2:
            sum_of_letters = sum_of_letters + one_digits[integer]
            continue

        if len(str(integer)) == 2:
            if integer % 10 == 0:
                sum_of_letters = sum_of_letters + tens[int(integer / 10)]
                continue
            if integer < 20:
                sum_of_letters = sum_of_letters + teens[integer]
                continue
            else:
                sum_of_letters = sum_of_letters + tens[int(integer / 10)] + one_digits[integer % 10]
                continue
        if integer == 100:
            sum_of_letters = sum_of_letters + hundred + 3
            continue
        if integer % 100 == 0:
            sum_of_letters = sum_of_letters + one_digits[int(integer / 100)] + hundred
            continue
        sum_of_letters = sum_of_letters + one_digits[int(integer / 100)] + hundred + 3

        if integer % 100 < 10:
            sum_of_letters = sum_of_letters + one_digits[integer % 100]
            continue
        if (integer % 100) % 10 == 0:
            sum_of_letters = sum_of_letters + tens[int((integer % 100) / 10)]
            continue
        if integer % 100 < 20:
            sum_of_letters = sum_of_letters + teens[integer % 100]
            continue
        sum_of_letters = sum_of_letters + tens[int((integer % 100) / 10)] + one_digits[(integer % 100) % 10]

    print(sum_of_letters)


letters(1, 1000)
