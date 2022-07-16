with open('sample_words.txt', 'r') as words:
    print(words.read())
    pass
print()
with open('sample_words.txt', 'r') as words:
    print(words.read(22))
    pass
print()
with open('sample_words.txt', 'r') as words:
    print(words.readlines(22))
    pass
