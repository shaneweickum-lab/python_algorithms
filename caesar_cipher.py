

word = input('Enter in a word: ')
key = int(input("Now select your key to shift by (e.g. 3): "))

def shift_word(word, key):
    result = ""
    for char in word:
        if 'A' <= char <= 'Z':
            result += chr((ord(char) - 65 + key) % 26 + 65)
        elif 'a' <= char <= 'z':
            result += chr((ord(char) - 97 + key) % 26 + 97)
        else:
            result += char
    return result

shifted_word = shift_word(word, key)
print(f"The shifted word is: {shifted_word}")