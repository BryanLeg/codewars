# Define a function that removes duplicates from an array of non negative numbers and returns it as a result.

# The order of the sequence has to stay the same.

def distinct(seq):
    diff = []
    for i in range(len(seq)):
        if seq[i] not in diff:
            diff.append(seq[i])
    return diff

