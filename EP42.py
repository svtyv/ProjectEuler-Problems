import string

with open("0042_words.txt") as f:
    words = f.read()

w_l = words.replace('"', '').split(",")
alphabet = string.ascii_uppercase
alphabet_numerated = {l: n for n, l in enumerate(alphabet, 1)}


def triangle_number(numb: int):
    tn = 0
    n = 1
    while tn < numb:
        tn = int((n * (n + 1)) / 2)
        n += 1
    if tn == numb:
        return True
    else:
        return False


def alphaphet_summation(word: str) -> int:
    sum_of_letters = 0
    for letter in word:
        sum_of_letters += alphabet_numerated[letter]
    return sum_of_letters


for possible_triangle in w_l[:]:
    word_sum = alphaphet_summation(possible_triangle)
    if not triangle_number(word_sum):
        w_l.remove(possible_triangle)
print(len(w_l))
