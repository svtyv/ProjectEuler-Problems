def get_multiples(num_range: int, multiplier: int) -> []:
    multiples = []
    for n in range(num_range):
        multiple = (n + 1) * multiplier
        multiples.append(multiple)
    return multiples


def filter_array(multiples: [], excluded_numbers: []) -> []:
    # Or could do this, but harder to understand whats going on
    # return list(filter(
    #    lambda element: element not in excluded_numbers, multiples
    #))
    filtered_array = []
    for element in multiples:
        if element not in excluded_numbers:
            filtered_array.append(element)
    return filtered_array


if __name__ == '__main__':
    multiples_of_three = get_multiples(333, 3)
    multiples_of_five = get_multiples(199, 5)
    filtered_multiples_of_three = filter_array(
        multiples=multiples_of_three,
        excluded_numbers=multiples_of_five
    )
    total = sum(filtered_multiples_of_three) + sum(multiples_of_five)
    print(total)