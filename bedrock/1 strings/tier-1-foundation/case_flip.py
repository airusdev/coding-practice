def swap_case(string: str) -> str:
    output = ""

    for char in string:
        if char.islower():
            output += char.upper()
        else:
            output += char.lower()

    return output

samples = ['hello  hi', '5heLLo5', 'hI!#']

for sample in samples:
    output = swap_case(sample)
    print(output, end="\n")



""" THOUGHT PROCESS

from how i understand it, if a substring is lower_case, make it upper_case
if a substring is upper_case, make it lower_case
if spaces were encountered? continue
trailing and beginning spaces? i think it's best to ignore
make sure to check if its an 

step 1: step-by-step algorithm
    initialize an empty string
    loop from the first substring to the end of the string
    if a substring is a space -> add as is (ignore)
    if a substring is lower, add it to the output string but uppercase
    else add it to the output string but lowercase
    return the output string

step 2: core algorithm
    if space add as it is
    if lowercase substring -> return uppercase
    if uppercase substring -> return lowercase
    return new string

step 3: data structure to use
    no data structure, just if condition

step 4: cases
    if substring return its opposite case

step 5: edge cases
    spaces and numbers and symbols can just be added as is

step 6: pseudocode / sharpening of pseudocode

output = ""

for char in string:
    if char.islower():
        output += char.upper()
    else:
        output += char.lower()

return output

"""
