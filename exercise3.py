# Write a function that counts the number of vowels in a text 
# and stores that number in a dictionary, where the key is the 
# vowel and the value is the number of times that vowel appears 
# in the text. The function must take the text as an input parameter, 
# and return the dictionary.

def count_vowels(text):

    count_a = 0
    count_e = 0
    count_i = 0
    count_o = 0
    count_u = 0

    for letter in text:
        if letter == 'a':
            count_a = count_a + 1
        elif letter == 'A':
            count_a = count_a + 1
        else:
            continue

    for letter in text:
        if letter == 'e':
            count_e = count_e + 1
        elif letter == 'E':
            count_e = count_e + 1
        else:
            continue

    for letter in text:
        if letter == 'i':
            count_i = count_i + 1
        elif letter == 'I':
            count_i = count_i + 1
        else:
            continue

    for letter in text:        
        if letter == 'o':
            count_o = count_o + 1
        elif letter == 'O':
            count_o = count_o + 1
        else:
            continue

    for letter in text:
        if letter == 'u':
            count_u = count_u + 1
        elif letter == 'U':
            count_u = count_u + 1
        else:
            continue

    
    vowels = {'a': count_a, 'e': count_e, 
    'i': count_i, 'o': count_o, 'u': count_u}

    return vowels
    
text = input("Insert your text here: ")
vowels_qty = count_vowels(text)
print(vowels_qty)