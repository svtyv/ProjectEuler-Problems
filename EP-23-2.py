import json
import time
from typing import List, Dict

ABUNDANT_NUMBERS_FILE_PATH = "EP-23/abundant_numbers.json"

MAX_NUMBER = 28123


def main():
    abundant_numbers = _get_abundant_numbers()
    start = time.time()
    numbers = _get_non_summing_numbers(abundant_numbers)
    print(f"Result: {sum(numbers)}")
    print(f"Total runtime: {time.time() - start}")


def _get_abundant_numbers() -> List[int]:
    with open(ABUNDANT_NUMBERS_FILE_PATH, "r") as f:
        return json.loads(f.read())


def _get_non_summing_numbers(abundant_numbers: List[int]) -> List[int]:
    # Find all ints that cannot be written as the sum of two abundant numbers
    sums = _get_all_sums(abundant_numbers)
    numbers: List[int] = []
    for i in range(1, MAX_NUMBER + 1):
        if i not in sums:
            numbers.append(i)
    return numbers


def _get_all_sums(numbers: List[int]) -> Dict:
    sums = {}
    for i in numbers:
        for j in numbers:
            sums[i + j] = 1
    return sums


if __name__ == '__main__':
    main()
