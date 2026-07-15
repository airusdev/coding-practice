def vowel_census(string: str) -> int:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    total_count = 0

    for sub in string:
        if sub.lower() in vowels:
            total_count += 1

    return total_count

sample = "HELLO" # 2
output = vowel_census(sample)
print(output)

"""
PSEUDOCODE

step 1: understand what the problem is going to do in a step-by-step format
    general task: count vowels in a string
    a. start with the first letter of the string
    b. check if it is a vowel or not
    c. if it is a vowel, add 1 to the total count
    d. after repeating for all of the letters, return the total count

step 2: in one to three sentences, explain the program's core logic:
    check if a letter is a vowel, if it's a vowel, add one to the total count

step 3: figure out the essential data structure
    we need a way to find out if a letter is a vowel
    how?
    using a set, (O(1) lookup), and ensures each element is unique is what we'll use to store the vowels
    vowels = {'a', 'e', 'i', 'o', 'u'}

step 4: cases and conditions
    we're only checking if its a vowel or not
    if vowel, add one
    if not vowel, disregard

step 5: edge cases
    not much edge cases

step 6: sharped already

pseudocode:
vowels = {'a', 'e', 'i', 'o', 'u'}
total_count = 0

for sub in string:
    if sub in vowels:
        total_count += 1

return total_count
"""