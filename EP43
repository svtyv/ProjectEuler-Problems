import itertools
import functools

x = "1234567890"

tuples_of_permutations = list(itertools.permutations(x))

list_of_permutations = []
for i in tuples_of_permutations:
    if int(i[3]) % 2 == 0 and int(i[5]) % 5 == 0 and (int(i[5]) - int(i[6]) + int(i[7])) % 11 == 0:
        list_of_permutations.append(functools.reduce(lambda x, y: x + y, list(i)))

for i in list_of_permutations[:]:
    if int(i[2:5]) % 3 != 0:
        list_of_permutations.remove(i)
        continue
for i in list_of_permutations[:]:
    if int(i[4:7]) % 7 != 0:
        list_of_permutations.remove(i)
        continue
for i in list_of_permutations[:]:
    if int(i[6:9]) % 13 != 0:
        list_of_permutations.remove(i)
        continue
for i in list_of_permutations[:]:
    if int(i[7:]) % 17 != 0:
        list_of_permutations.remove(i)
        continue
the_sum = 0
for i in list_of_permutations:
    the_sum += int(i)
print(the_sum)
