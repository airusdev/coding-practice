#!/bin/python3

def super_reduced_string(s):
    stack = []

    for sub in s:
        if len(stack) == 0 or sub != stack[-1]:
            stack.append(sub)
        elif stack[-1] == sub:
            stack.pop(-1)

    if not stack:
        return "Empty String"
    else:
        return "".join(stack)


# expected_output = "tqauhujtmxnsbzpykwlvpfyqijvdhuhirdmuxiobyvxupqwydkpbxmfvxhgicuzdealkgxlfmjiucasokrdznmtlwh"
# string = "zztqooauhujtmxnsbzpykwlvpfyqijvdhuhiroodmuxiobyvwwxupqwydkpeebxmfvxhgicuzdealkgxlfmjiucasokrdznmtlwh"
expected_output = "bacdcheo"
string = "aabacdchello"
output = super_reduced_string(string)

# for i in range(0, len(output)):
#     if output[i] != expected_output[i]:
#         print(output[i])
#         break

print(output == expected_output)
print(f"output: {output}")
