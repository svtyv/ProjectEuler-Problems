import numpy as np

dict_of_squares = {}
list_of_squares = []
for i in range(1, 501):
    dict_of_squares[i ** 2] = i
    list_of_squares.append(i ** 2)


def square_differences(larger_square: int, smaller_square: int):
    the_difference = larger_square - smaller_square
    if the_difference in dict_of_squares:
        return np.array([np.sqrt(larger_square), np.sqrt(smaller_square), np.sqrt(the_difference)]).astype(int)
    else:
        return "0"


triangle_sets = []
for larger in list_of_squares[3:]:
    for smaller in list_of_squares[:list_of_squares.index(larger)]:
        x = square_differences(larger, smaller)
        if len(x) > 1:
            triangle_sets.append(x)
dic_of_triangles = {}
for triangle in triangle_sets[:]:
    if np.sum(triangle) in dic_of_triangles:
        dic_of_triangles[np.sum(triangle)] += 1
        continue
    else:
        dic_of_triangles[np.sum(triangle)] = 1
list_of_triangles = []
for i in dic_of_triangles:
    list_of_triangles.append([i, dic_of_triangles[i]])
highest = [[0, 0]]
for i in list_of_triangles:
    if i[1] > highest[0][1]:
        highest.clear()
        highest.append(i)
print(highest)
