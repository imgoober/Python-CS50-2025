def shorten(word):
    vowels = ['A', 'a', "E", 'e', "I", 'i', "O", 'o', "U", 'u']

    final_word = ""

    for i in word:
        if i not in vowels:
            final_word = final_word + i

    return final_word
