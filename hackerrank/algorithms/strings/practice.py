#!/bin/python3

def super_reduced_string(s):
    stack = [s[0]]
    print(stack[len(stack) - 1])
    
    for letter in s:
        print(letter)
        print(stack)
        if letter not in stack:
            stack.append(letter)
        elif (stack.index(letter) == len(stack) - 1):
            stack.remove(letter)
            continue

    if not stack:
        return "Empty String"
    else:
        return "".join(stack)


expected_output = "tqauhujtmxnsbzpykwlvpfyqijvdhuhirdmuxiobyvxupqwydkpbxmfvxhgicuzdealkgxlfmjiucasokrdznmtlwh"
string = "zztqooauhujtmxnsbzpykwlvpfyqijvdhuhiroodmuxiobyvwwxupqwydkpeebxmfvxhgicuzdealkgxlfmjiucasokrdznmtlwh"
output = super_reduced_string(string)

# for i in range(0, len(output)):
#     if output[i] != expected_output[i]:
#         print(output[i])
#         break

print(output == expected_output)
