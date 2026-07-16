def title_case(string: str) -> str:
    string = string.split()
    new_string = []

    for i in range(0, len(string)):
        word = string[i]
        string[i] = word[0].upper() + word[1::].lower()
    
    return " ".join(string)

samples = ['hi yes hi', 'HIIII yes hELLO', '1293124 1wu5123 423']

for sample in samples:
    output = title_case(sample)
    print(output)
