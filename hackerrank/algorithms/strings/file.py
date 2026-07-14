s = ''
stack = []


print(len(stack) == 0)


def super_reduced_string(s):
    stack = [s[0]]
    
    for i in range(1, len(s)):
        letter = s[i]

        if letter != stack[i - 1]:
                stack.append(letter)


# orig:
    # for letter in s:
    #     print(letter)
    #     print(stack)
    #     if letter not in stack:
    #         stack.append(letter)
    #     elif (stack.index(letter) == len(stack) - 1):
    #         stack.remove(letter)
    #         continue