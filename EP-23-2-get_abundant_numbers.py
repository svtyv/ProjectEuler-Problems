import json
import os
import time
from typing import List

MAX_NUMBER = 28123


def main(file_path: str):
    abundant_numbers = _get_abundant_numbers()
    print(len(abundant_numbers))

    file_dir = "/".join(file_path.split("/")[:-1])
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    with open(file_path, "w") as f:
        f.write(json.dumps(abundant_numbers))


def _get_abundant_numbers() -> List[int]:
    start = time.time()
    abundant_numbers: List[int] = []
    for i in range(12, MAX_NUMBER + 1):
        if i % 2 != 0 and i % 5 != 0:
            continue
        divisors = _get_divisors(i)
        if sum(divisors) > i:
            abundant_numbers.append(i)
    print(f"abundant numbers finding time: {time.time() - start}")
    return abundant_numbers


def _get_divisors(number: int) -> List[int]:
    if number < 0:
        # error
        return []
    if number == 1:
        return [1]
    divisors: List[int] = [1]
    for i in range(2, number):
        if number % i == 0:
            divisors.append(i)
    return divisors


if __name__ == '__main__':
    main("EP-23/abundant_numbers.json")
