# !/usr/bin/python3

def balanced_brackets(brackets: str) -> str:
    stack = []
    dict_ = {
    "(": ")",
    "{": "}",
    "[": "]"
    }

    for bracket in brackets:
        if bracket in dict_:
            stack.append(bracket)
        elif not stack:
            return "NOT BALANCED"
        else:
            if dict_.get(stack[-1]) == bracket:
                stack.pop(-1)
            else:
                return "NOT BALANCED"

    if stack:
        return "NOT BALANCED"

    return "BALANCED"

string = "{[()]}" # balanced
string = "{[}]" # not balanced
output = balanced_brackets(string)
print(output)

"""
{[()]}
dict = {
    "(": ")",
    "{": "}",
    "[": "]"
}
stack = []

for bracket in brackets:
    if bracket in dict:
        stack.append(bracket)
    elif not stack:
        return "NOT BALANCED"
    else:
        if dict.get(stack[-1]) == bracket:
            stack.pop(-1)
        else:
            return "NOT BALANCED"

if stack:
    return "NOT BALANCED"
"""

"""
what we did in this session: (pseudocode)
    1. first, try to understand what the program is going to do step-by-step given some input
    2. in one to three sentence/s, explain in a nutshell the program's core logic
    3. figure out the essential data structure to solve this problem
    4. think of the specific cases and conditions and what to do in those instances
    5. think of edge cases and what to do accomodate those
    6. merge cases and edges into ordered steps (sharpen)
    7. code.
"""
