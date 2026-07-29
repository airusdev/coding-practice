def window_sum(arr: list[int], k: int):
    window_sum = sum(arr[:k])
    greatest = window_sum

    for i in range(0, len(arr) - k):
        window_sum -= arr[i]
        window_sum += arr[i+k]

        if window_sum > greatest:
            greatest = window_sum

    return greatest

tests = [
    ([2, 1, 5, 1, 3, 2], 3, 9),
    ([1, 1, 1, 1, 1], 2, 2),
    ([4, -1, 2, 1, -5, 3], 2, 3),
    ([5], 1, 5),
    ([-2, -1, -3, -4], 2, -3),
    ([10, 20, 30, 40, 50], 5, 150),
    ([3, 3, 3, 3], 2, 6),
]

for arr, k, expected in tests:
    output = window_sum(arr, k)
    if output == expected:
        print("PASS")
    else:
        print("FAIL")


"""

2 1 5 1 3 2


"""