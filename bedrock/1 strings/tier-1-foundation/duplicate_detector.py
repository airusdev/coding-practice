def duplicate_detector(string: str) -> str:
    string = "".join(string.lower().split())
    seen = set()
    for letter in string:
        if letter not in seen:
            seen.add(letter)
        else:
            return letter

    return "NO REPEATED CHARACTER"

samples = ["hello", "R a C e C a r", ""]
for sample in samples:
    output = duplicate_detector(sample)
    print(f"input: {sample}\noutput: {output}\n")

"""
THOUGHT PROCESS

step 1: step-by-step algorithm
    initialize a set to store the seen substrings
    start with the first letter of the string and loop through all of it
    if the letter is not in the set yet, add it to the set
    if the letter is in the set, return letter
    if no repeated characters then return "NO REPEATED CHARACTERS"

step 2: core logic
    if a letter is not in the set, add it
    if the letter is in the set, return it thats the first repeated character
    if no repeated character, return NO REPEATED CHARACTER

step 3: data structure
    use a set because O(1) lookup and is unique

step 4: cases
    cases are if there is a repeated character then return that
    if not, return NO FIRST REPEATED CHARACTER

step 5: edge cases
    remove any trailing / spaces, we're not going to take into account the spaces
    lowercase all the letters
    if string is empty, we'll return no repeated character

step 6: pseudocode / sharpening

string = "".join(string.lower().split())
seen = {}
for letter in string:
    if letter not in seen:
        seen.add(letter)
    else:
        return letter

return "NO REPEATED CHARACTER"

step 7: code

error in step 6: instead of doing set() i did {}
"""