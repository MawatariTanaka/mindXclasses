demo = open("demo.txt", "w")
demo.write('Sample text')
demo.close()

demo = open('demo.txt', 'r')
print(demo.read())
