

def palindrome_check(string: str) -> None:
    string = string.lower().replace(" ", "")

    for first in range(0, len(string) // 2):
        second = len(string) - first - 1

        if string[first] != string[second]:
            return False

    return True

sample = "racecar"
sample1 = 'rAce car'

output = palindrome_check(sample)
output1 = palindrome_check(sample1)

print(output)
print(output1)
