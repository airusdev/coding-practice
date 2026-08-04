def consecutive_ones(string: str, k: int) -> int:
    largest = 0
    zero_counter = 0
    left_i = 0

    for right in range(0, len(string)):




"""
EXAMPLE
[1, 1, 0], 3
[1, 1, 0, 0], 1

largest = 2
zero_counter = 0
left_i = 0

expand by right
    current_window = [1]
    current_element = 1

is it 0? nah
is len(current_window) > largest? yes: largest = len(current_window)
largest = 1


expand by right
    current_window = [1, 1]
    current_element = 1

is it 0? nah
is len(current_window) > largest? yes: largest = len(current_window)
largest = 2


expand by right
    current_window = [1, 1, 0]
    current_element = 0

is current_element == 0?
    yes
        zero_counter -= 1 (zero_counter = 1)
        window = [1, 1, 1]

"""
