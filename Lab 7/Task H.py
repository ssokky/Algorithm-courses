def encrypt_word(word):
    encrypted_word = ''
    for char in word:
        if char.isalpha():
            shift = len(word)
            if char.islower():
                encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            encrypted_word += encrypted_char
        else:
            encrypted_word += char
    return encrypted_word

def encrypt_string(input_string):
    words = input_string.split()
    encrypted_words = [encrypt_word(word) for word in words]
    return ' '.join(encrypted_words)

input_string = input()

result = encrypt_string(input_string)
print(result)
