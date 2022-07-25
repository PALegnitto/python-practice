def print_upper_words(list_of_words):
    """takes a list of words and returns them in uppercase"""
    
    for word in list_of_words:
        if word[0] == 'e' or word[0] == 'E':
            print(word.upper())

        
list_o_words = ['hello','test', 'eel', 'tacos']
print_upper_words(list_o_words)
    