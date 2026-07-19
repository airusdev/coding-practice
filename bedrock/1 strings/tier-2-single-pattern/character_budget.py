def character_budget(string: str, k: int) -> int:
    largest = 0
    freq = {}
    i = 0

    for right in range(0, len(string)):
        if string[right] not in freq:
            freq[string[right]] = 1
        else:
            freq[string[right]] += 1
        
        while len(freq) > k:
            left = string[i]
            
            if freq[left] > 1:
                freq[left] -= 1
            else:
                del freq[left]
            
            i += 1
        
        total_occurrences = right - i + 1

        if total_occurrences > largest:
            largest = total_occurrences

    return largest

tests = [
    ("eceba", 2, 3),
    ("aabacbebebe", 3, 7),
    ("aaaa", 2, 4),
    ("a", 2, 1),
    ("abcadcacacaca", 3, 11),
    ("eceba", 1, 1),
    ("", 2, 0),
]
 
for string, k, expected in tests:
    result = character_budget(string, k)
    status = "PASS" if result == expected else "FAIL"
    print(f"{status} | input: {string!r}, k={k} | expected: {expected}, got: {result}\n")


""" THINKING

'eceba'

step 1: step-by-step algorithm
    initialize largest variable = 0
    initialize frequency char = {}
    
    expand window to the right by 1: 'e'
    add 'e' to the frequency char e: 1
    while len(freq) > 2:
        reduce window from left by 1
        if freq[string[starting_index]] > 1:
            freq[string[starting_index]] -= 1
        else:
            remove freq[string[starting_index]]
        
    are there more than 2 distinct chars? no
    if len(frequency char) > largest variable, var = len(frequency char)
    
    repeat

largest = 0
freq = {}
i = 0

for left in range(0, len(string)):
    if left not in freq:
        freq[string[left]] = 1
    else:
        freq[string[left]] += 1
    
    # if there are more than 2 distinct characters, remove/reduce occurrence of letter
    while len(freq) > 2:
        if freq[string[left]] > 1:
            freq[string[left]] -= 1
        else:
            del freq[string[left]]
    
    # get the total occurrences of all letters 
    total_occurrences = 0
    for value in freq.values():
        total_occurrences += value
    
    if total_occurrences > largest:
        largest = total_occurrences


my whole process:
    i first understood what the problem wants me to do.
        what's the input and expected output
    i vaguely trace through the example input step-by-step to get some idea on what the algorithm should do
    afterwards, decide on the data structure we're going to use
    what variables to use to track information

    write the vague step-by-step into real code and make sure to sharpen and trace through the logic in the mind as we write it
    sharpen it once more and verify
    write test cases
    if it passes: optimize
    else: improve the logic
    
notes for this: i could simplify acquiring the total occurrences by doing right - i + 1
"""