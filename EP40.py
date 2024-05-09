import numpy as np

file_open = open("champer.txt", "r")
champer = file_open.read()

numbers_to_multiply = np.array(
    [champer[0], champer[9], champer[99], champer[999], champer[9999], champer[99999], champer[999999]])
result = np.prod(numbers_to_multiply.astype(int))
print(result)

file_open.close()
