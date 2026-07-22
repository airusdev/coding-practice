def clean_palindrome(string: str) -> bool:
    clean_string = [char.lower() for char in string if char.isalpha()]

    for left in range(0, len(clean_string)):
        right = len(clean_string) - 1 - left
        
        if clean_string[left] != clean_string[right]:
            return False
    
    return True


tests = [
    ('hello', False),
    ('oll E% 12h', False),
    ('r a  #%$ce((*$#830))car', True),
    ('', True),
]

for sample, expected in tests:
    output = clean_palindrome(sample)
    
    if output == expected:
        print("PASS!")
    else:
        print("FAIL!")


"""

i first need a way to lowercase the given string, remove spaces, and remove any char that is not a letter
so it only inputs lowercased chars to ensure accuracy in checking if its a paldinrome

"""