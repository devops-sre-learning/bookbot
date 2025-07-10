

def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_characters(text):
    letters = {}
    for letter in text:
        letter = letter.lower()
        if letter not in letters:
            letters[letter] = 1
        else:
            letters[letter]+=1
    return letters


        


