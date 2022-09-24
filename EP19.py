def sundays():
    n = 1
    sunday_counter = 0
    weekday = 2
    while n < 100:
        if weekday % 7 == 0:
            sunday_counter += 2
        if weekday % 7 == 1:
            sunday_counter += 2
        if weekday % 7 == 2:
            sunday_counter += 2
        if weekday % 7 == 3:
            sunday_counter += 1
        if weekday % 7 == 4:
            sunday_counter += 3
        if weekday % 7 == 5:
            sunday_counter += 1
        if weekday % 7 == 6:
            sunday_counter += 1
        if weekday % 4 == 0:
            weekday += 2
        else:
            weekday += 1
        n += 1
    return sunday_counter


print(sundays())
