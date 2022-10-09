from typing import List

CHAR_START = 64


def main():
    names_sorted = sorted(_read_names("names.txt"))
    total = _get_total_score(names_sorted)
    print(total)


def _read_names(filename: str) -> List[str]:
    with open(filename, "r") as file:
        file_content = file.read()
    names = file_content.split(",")
    return [n.replace('"', "") for n in names]


def _get_total_score(names_sorted) -> int:
    total = 0
    for i in range(len(names_sorted)):
        total += (i + 1) * _get_alphabetical_value(names_sorted[i])
    return total


def _get_alphabetical_value(name: str) -> int:
    return sum([ord(c) - CHAR_START for c in name])


if __name__ == '__main__':
    main()
