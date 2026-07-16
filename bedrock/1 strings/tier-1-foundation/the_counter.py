def count_occurrences(string: str, given_char: str) -> dict[int]:
    total_count = 0

    for char in string:
        if char == given_char:
            total_count += 1

    return total_count


samples = [('hello hi', 'h'), ('world yes yes yo', 'y'), ('hiii', 'i'), ('hello', 'a')]

for sample in samples:
    print(f"string: {sample[0]} char: {sample[1]}")
    output = count_occurrences(sample[0], sample[1])
    print(output, end="\n")
