from decimal import *

getcontext().prec = 1000


def main():
    removable_reciprocals = []
    for i in denominators(1000):
        decimal_part = reciprocal_decimals(i, 16)
        decimal_part = str(decimal_part)
        if decimal_part[3:7] in decimal_part[8:]:
            removable_reciprocals.append(i)
    a = denominators(1000)
    for i in a[:]:
        if i in removable_reciprocals:
            a.remove(i)
            continue

    c = []
    for i in a:
        b = str((Decimal(1) / Decimal(i)) * 10 ** 101)
        if b[10:71] in b[72:]:
            c.append(i)
    for i in a[:]:
        if i in c:
            a.remove(i)

    print(a)  # gives 8 answers. It's the last one 983


def denominators(highest: int) -> list:
    denominators_list = []
    for i in range(1, highest + 1):
        rec = str(1 / i)
        if len(rec) < 10:
            continue
        else:
            denominators_list.append(i)

    return denominators_list


def reciprocal_decimals(denominator: int, decimals: int) -> int:
    reciprocal = int((denominator ** -1) * 10 ** decimals)
    return reciprocal


if __name__ == "__main__":
    main()
