keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

# Từ điển cần trả về
# dictionary = dict(zip(keys, values))
dictionary = {}
for i in range(len(keys)):
    dictionary[keys[i]] = values[i]

print(dictionary)
