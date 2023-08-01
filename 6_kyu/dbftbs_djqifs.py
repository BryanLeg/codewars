# Caesar Ciphers are one of the most basic forms of encryption. It consists of a message and a key, and it shifts the letters of the message for the value of the key.

# Read more about it here: https://en.wikipedia.org/wiki/Caesar_cipher
# Your task

# Your task is to create a function encryptor that takes 2 arguments - key and message - and returns the encrypted message.

# Make sure to only shift letters, and be sure to keep the cases of the letters the same. All punctuation, numbers, spaces, and so on should remain the same.

# Also be aware of keys greater than 26 and less than -26. There's only 26 letters in the alphabet!
# Examples

# A message 'Caesar Cipher' and a key of 1 returns 'Dbftbs Djqifs'.

# A message 'Caesar Cipher' and a key of -1 returns 'Bzdrzq Bhogdq'.

# "".join(list(alph[alph.index(x.lower()) + (key%26)] for x in message if x!=' '))
import re

def encryptor(key, message):
    alph_lower = list(map(chr, range(97, 123)))
    alph_upper = list(map(chr, range(65, 91)))
    return "".join(list(map(lambda x: alph_lower[(alph_lower.index(x) + key)%26] if x.islower() else alph_upper[(alph_upper.index(x) + key)%26] if x.isupper() else x, message)))

print(encryptor(13, 'Caesar Cipher'))