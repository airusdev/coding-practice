def frequency_map(string: str) -> dict[str, int]:
    frequency = {}
    
    for char in string:
        if char not in frequency:
            frequency[char] = 1
        else:
            frequency[char] += 1
    
    return frequency
