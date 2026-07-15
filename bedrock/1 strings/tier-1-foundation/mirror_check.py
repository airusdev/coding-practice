def mirror_check(string: str) -> bool:
    string = "".join(string.lower().split()) # ensures the string is clean
    print(string)

    for first in range(0, len(string) // 2):
        second = len(string) - first - 1 # for example, first index = 0. len of string = 5 - 1 = 4, 4-0 = 4 last index is 4 which is correct
        if string[first] != string[second]:
            return False

    return True

sample = "racecar"
sample2 = "R A ce c A r"
output = mirror_check(sample)
output2 = mirror_check(sample2)

print(output)
print(output2)

"""
THOUGHT PROCESS

what is a palindrome? a palindrome is a string with substrings even if reversed are the same
example: racecar

step 1: step-by-step algorithm
    a. initialize a second "pointer" pointing to the last element of the string
    b. use a for i i range loop to have an index
    c. use the `i` index from the for i in range to access the elements
    d. if the element in the i index and in the second pointer are not the same, return False
    e. at the end of a loop, return True

step 2: in one sentence what is the core algorithm?
    create a second pointer. compare letter in the i index and in the second pointer. if they're not the same, return False
    at the end of the program, return true

step 3: what data structure?
    only variable to track the letter in the second element
    
step 4: cases
    if string[i] != string[second_pointer] return False
    at the end of the string, if all are the same, return True

step 5: edge cases
    should accomodate both small or capital words
    remove spaces/any trailing at the beginning and at the end

step 6: pseudocode / sharpen pseudocode
given input: string
string = "".join(string.lower().split()) # ensures the string is clean

for first in range(0, len(string)):
    second = len(string) - first - 1 # for example, first index = 0. len of string = 5 - 1 = 4, 4-0 = 4 last index is 4 which is correct
    if string[first] != string[second]:
        return False

return True

step 7: code

errors in my steps:
    at step 6, i didnt sharpen the pseudocode enough. i forgot about adding "string[]" to 'first' and 'second'
    at step 6 also, i didnt think of adding a divide by 2 to ensure each substring only gets checked once.
"""