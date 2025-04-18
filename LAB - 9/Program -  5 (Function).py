def ispangram(sentence):
    
    alphabet_set = set('abcdefghijklmnopqrstuvwxyz')
    
    sentence_set = set(sentence.lower())
    
    return alphabet_set <= sentence_set

test_sentences = [
    "The quick brown fox jumps over the lazy dog",
    "Crazy Fredrick bought many very exquisite opal jewels"
]

for sentence in test_sentences:
    if ispangram(sentence):
        print(f'"{sentence}" is a pangram.')
    else:
        print(f'"{sentence}" is not a pangram.')
        
