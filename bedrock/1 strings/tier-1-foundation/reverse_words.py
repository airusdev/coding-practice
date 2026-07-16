def reverse_words(sentence: str) -> str:
    sentence = sentence.split(" ")
    new_sentence = []
    
    for i in range(len(sentence) - 1, -1, -1):
        new_sentence.append(sentence[i])
    
    return " ".join(new_sentence) 

samples = ['hello world hi yes', 'yes hi hello oh yeah']

for sample in samples:
    output = reverse_words(sample)
    print(output, end="\n")
