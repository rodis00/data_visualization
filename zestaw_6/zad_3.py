import string

print(len(string.ascii_lowercase))
dict = string.ascii_lowercase

for letter in dict:
    for x in range(len(dict)):
        print(letter+letter+string.ascii_lowercase[x]+', ', end='')
    print('')