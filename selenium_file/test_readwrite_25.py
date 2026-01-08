

# file = open('text.txt')
# print(file.read(10))
# print(file.readline())
# print(file.readlines())

#print line by line text using readline

# file = open('text.txt')
# line = file.readline()
# while line != "":
#     print(line)
#     line = file.readline()

# print line by line text using readlines
# file = open('text.txt')
# for line in file.readlines():
#     print(line)

# reverse the list the write mode
with open('text.txt') as reader:
    content = reader.readlines()
    reversed(content)
    with open('text.txt', "w") as writer:
        for line in reversed(content):
            print(line)
