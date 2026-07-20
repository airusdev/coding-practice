def first_unique_char(string: str) -> int:
    string = string.replace(" ", "")
    freq = {}
    
    for char in string:
        if char.lower() not in freq:
            freq[char.lower()] = (1, char)
        else:
            freq[char.lower()] = (freq[char.lower()][0] + 1, char)
    
    for key, value in freq.items():
        if value[0] == 1:
            return value[1]


tests = [
    ("hello", "h"),
    ("hheello", "o"),
    ("H h E e l O o", "l"),
    ("aabbcc", None),           # no unique character at all
    ("z", "z"),                 # single character
    ("", None),                 # empty string
    ("abcabc", None),           # every char repeats
    ("xxyz", "y"),              # unique char in the middle
    ("aabbx", "x"),             # unique char at the very end
    ("Aa Bb C", "C"),           # case-insensitive, spaces ignored, unique at end
]
    
for sample, expected in tests:
    output = first_unique_char(sample)
    if output == expected:
        print("PASS")
    else:
        print("FAIL")


"""


essentially, we're going to return the index of the first non repeating char
meaning: the index of the first char that doesnt repeat


first method:
what if acquire all of the occurrences first
return the first key with only 1 value

we have no way to be sure if the char we're currently on only has one


initialize a freq dict: {}
for letter in string:
    if letter not in string:
        freq[letter] = 1
    else:
        freq[letter] += 1

for key, value in freq.items():
    if value == 1:
        return key

"""