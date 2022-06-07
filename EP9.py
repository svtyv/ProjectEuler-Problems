def pythagorean_triplet():
    sums = []
    triplet = []
    for i in range(2, 998):
        for j in range(2, i):
            if i + j > 1000:
                break
            for k in range(2, j):
                if i + j + k == 1000:
                    x = [i, j, k]
                    sums.append(x)
    for alist in sums:
        if alist[0] ** 2 == alist[1] ** 2 + alist[2] ** 2:
            triplet.append(alist)
    product = triplet[0]
    product = product[0] * product[1] * product[2]

    print(product)


pythagorean_triplet()
