import numpy as np


def concatenator(number1: int, number2: int) -> int:
    number1_str = str(number1)
    number2_str = str(number2)
    concatenated_number = number1_str + number2_str
    return int(concatenated_number)


multipliers_list = []
for i in range(1, 9999):
    multipliers_list.append(i)
multipliers_arr = np.array(multipliers_list)
multipliers_arr = multipliers_arr[multipliers_arr % 10 != 0]
concatenated_numbers = []

for i in multipliers_arr:
    long_boy = i
    for b in range(2, 10):
        long_boy = concatenator(long_boy, i * b)
        if len(str(long_boy)) == 9:
            concatenated_numbers.append(long_boy)
            break
        elif len(str(long_boy)) > 9:
            break
        else:
            continue

concatenated_numbers = sorted(list(np.array(concatenated_numbers).astype(str)))

for n in concatenated_numbers[:]:
    if "0" in n:
        concatenated_numbers.remove(n)
        continue
    elif len(set(n)) < 9:
        concatenated_numbers.remove(n)
        continue
    else:
        continue
print(max(concatenated_numbers))
