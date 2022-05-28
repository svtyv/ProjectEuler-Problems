
def multiplying(multiplesOfThree,multiplesOfFive):
    multiplesOfThree = []
    multiplesOfFive = []
    sum = int(0)
    n = int(1)
    while n <= 333:
        Three = n*3
        multiplesOfThree.append(Three)
        n += 1
    n = int(1)
    while n <= 199:
        Five = n*5
        multiplesOfFive.append(Five)
        n += 1
    for element in multiplesOfThree:
        if element in multiplesOfFive:
            multiplesOfThree.remove(element)
        else:
            pass

    return(multiplesOfFive, multiplesOfThree)

def theSumOfLists(list1,list2):
    sum1 = int(0)
    sum2 = int(0)
    total = int(0)
    for element in list1:
        sum1 = element + sum1
    for element in list2:
        sum2 = element + sum2
    total = sum1 + sum2
    return total



multiples = multiplying(3,5)
total = theSumOfLists(multiples[0],multiples[1])
print(total)


