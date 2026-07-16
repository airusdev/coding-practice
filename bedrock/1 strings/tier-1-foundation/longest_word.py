def longest_word(sentence: str) -> str:
    sentence = sentence.split(" ") 
    
    longest = 0
    longest_word = 's'
    
    for word in sentence:
        if len(word) > longest:
            longest = len(word)
            longest_word = word

    return longest_word
