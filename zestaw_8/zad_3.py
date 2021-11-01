list = [[x * y for x in range(1, 8)] for y in range(1, 8)]
print(list)


print('\nciekawostka')
print([x % 3 == 0 for x in range(1, 16)])
print([x for x in range(1, 16) if x % 3 == 0])

