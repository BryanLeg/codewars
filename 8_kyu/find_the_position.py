# When provided with a letter, return its position in the alphabet.

# Input :: "a"

# Ouput :: "Position of alphabet: 1"

def position(alphabet):
    return f'Position of alphabet: {list(map(chr, range(97, 123))).index(alphabet)+1}'