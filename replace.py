def replacePunctuation(text):
    new_text = []

    words = text.split()

    for word in words:
        for char in word:
            if char in string.punctuation:
                word = word.replace(char,' ')

        new_text.append(word)

    return ' '.join(new_text)
