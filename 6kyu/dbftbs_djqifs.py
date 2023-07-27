"""
Caesar Ciphers are one of the most basic forms of encryption. It consists of a message
and a key, and it shifts the letters of the message for the value of the key.

Your task is to create a function encryptor that takes 2 arguments - key and message -
and returns the encrypted message.
Make sure to only shift letters, and be sure to keep the cases of the letters the same.
All punctuation, numbers, spaces, and so on should remain the same.
Also be aware of keys greater than 26 and less than -26. There's only 26 letters in the
alphabet!

Examples
A message 'Caesar Cipher' and a key of 1 returns 'Dbftbs Djqifs'.
A message 'Caesar Cipher' and a key of -1 returns 'Bzdrzq Bhogdq'.
"""


import string

def encryptor(key, message):
    result_string = ""
    alphabet = string.ascii_lowercase
    for char in message:
        if char.lower() not in alphabet:
            result_string += char
        else:
            char_index = alphabet.index(char.lower())
            if char.upper() == char:
                result_string += alphabet[(char_index + key) % 26].upper()
            else:
                result_string += alphabet[(char_index + key) % 26]
    return result_string

print(encryptor(-64, 's'))
        
    