# Task 3

# Self-study positional arguments for Python scripts (sys.argv). 
# Write a script that takes a list of words (or even phrases)a Script should ask a user to write 
# something to stdin until user won't provide one of argument phrases.

import sys

dictionary = list()
for i in range(1, len(sys.argv)):
    buf = sys.argv[i]
    dictionary.append(buf)
    for j in range(i+1, len(sys.argv)):
        buf = ' '.join([buf, sys.argv[j]])
        dictionary.append(buf)    
    
while True:

    secret = input('Tell me your secret (word/phrase): ')

    if secret in dictionary:
        print('Nice! Your secret matches.')
        exit()
    elif secret in dictionary:
        print('Nice! Your secret matches.')
        exit()
    else:
        print('Bad secret, try again!')


# At first stage, a dictionary of pass words and phrases is being created.
# This dictionary contains all the words from arguments list and their combination 
# in *direct order* of any possible length. E.g., from the list ['a', 'b', 'c'] 
# the following dictionary will be created: ['a', 'a b', 'a b c', 'b c'], so there 
# is no 'a c' combination as this chars don't stand together.
# Thus, any number of words (in direct order) from arguments list can be accepted 
# as a secret word/phrase.
