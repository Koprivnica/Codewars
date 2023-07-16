"""
Implement a pseudo-encryption algorithm which given a string S and an integer N concatenates all the odd-indexed characters of S with
all the even-indexed characters of S, this process should be repeated N times.

Examples:
encrypt("012345", 1)  =>  "135024"
encrypt("012345", 2)  =>  "135024"  ->  "304152"
encrypt("012345", 3)  =>  "135024"  ->  "304152"  ->  "012345"

encrypt("01234", 1)  =>  "13024"
encrypt("01234", 2)  =>  "13024"  ->  "32104"
encrypt("01234", 3)  =>  "13024"  ->  "32104"  ->  "20314"

Together with the encryption function, you should also implement a decryption function which reverses the process.
If the string S is an empty value or the integer N is not positive, return the first argument without changes.
"""


def encrypt(text, n):
    if not text or n < 1:
        return text
    while n:
        text = text[1::2] + text[::2]
        n -= 1
    return text



print(encrypt("01234", 0))



def decrypt(encrypted_text, n):
    if not encrypted_text or n < 1:
        return encrypted_text
    
    text = list(encrypted_text)
    half = len(encrypted_text) // 2
    
    while n:
        text[1::2], text[::2] = text[:half], text[half:]
        n -= 1
    return "".join(text)


print(decrypt("01234", 1))        