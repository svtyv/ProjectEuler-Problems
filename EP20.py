def factorial():
    in_product = []
    for integers in range(1, 101):
        in_product.append(integers)
    for divisible in in_product:
        if divisible % 10 == 0:
            divided = int(divisible / 10)
            in_product.append(divided)
            in_product.remove(divisible)
    in_product = list(filter((1).__ne__, in_product))
    in_product.sort()
    the_product = 1
    for i in in_product:
        the_product = i*the_product
    the_product = str(the_product)
    the_product = list(map(int,the_product))
    the_product = list(filter((0).__ne__,the_product))
    the_sum = 0
    for i in the_product:
        the_sum += i



    print(the_sum)


factorial()
