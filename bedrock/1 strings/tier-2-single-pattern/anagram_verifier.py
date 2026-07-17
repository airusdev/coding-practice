def anagram_verifier(a: str, b: str) -> bool:
    a = a.lower().replace(' ', '')
    b = b.lower().replace(' ', '')

    if len(a) != len(b): return False

    a_frequency = {}
    b_frequency = {}

    # frequency check for string a
    for letter in a:
        if letter not in a_frequency:
            a_frequency[letter] = 1
        else:
            a_frequency[letter] += 1

    # frequency check for string b
    for letter in b:
        if letter not in b_frequency:
            b_frequency[letter] = 1
        else:
            b_frequency[letter] += 1

    return a_frequency == b_frequency

print(anagram_verifier('silent', 'listen'))

""" THOUGHT PROCESS

step 1: step-by-step algorithm
we first need a way to know the frequency of each letters and then compare them later on with another for loop
but if we do for loops just to check the frequency for a and frequency for b, that wont be very nice

instead:
turn a into a list
turn b into a list

a = [a, p, p, l, e]
b = [p, l, p, a, e]

for letter in a:
    if letter in b:
        b.remove(letter)
    else:
        return False

if b:
    return False
else:
    return True

"""