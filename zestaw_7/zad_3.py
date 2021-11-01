import string

for letter in string.ascii_uppercase:
    for i in range(len(string.ascii_uppercase)):
        print(letter+string.ascii_uppercase[i]+', ', end='')
    print('')

