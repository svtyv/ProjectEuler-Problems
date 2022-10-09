f = open("p022_names.txt", "r")
names_list = []
sum = 0
for n in f:
    names_list.append(n.replace('"', "").split(","))
names_list = sorted(names_list[0])

for name in names_list:
    for char in name:
        sum += ord(char) - 64
    sum *= (names_list.index(name) + 1)
    names_list[names_list.index(name)] = sum
    sum = 0
x = 0
for number in names_list:
    x += number

print(x)
