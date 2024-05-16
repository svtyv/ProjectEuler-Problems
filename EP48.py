x = [a for a in range(1, 1001)]
the_sum = 0
for i in x:
    the_sum += i ** i

print(the_sum % 10000000000) #gives ten last numbers
