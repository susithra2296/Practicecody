#read mode
# file = open('\\Users\\Susis\\PycharmProjects\\pythonProject\\python\\info.txt',"r")
# print(file.read())
# print(file.tell())
# file.seek(0)
# print(file.tell())
# print(file.read())
#read mode
# file = open('\\Users\\Susis\\PycharmProjects\\pythonProject\\python\\info.txt',"r")
# print(file.readline())
# print(file.readlines()) #listview
# print(file.read(10))  #first 10 char
# file.close()
#writemode
# file = open('\\Users\\Susis\\PycharmProjects\\pythonProject\\python\\info.txt',"w")
# file.write("adding new txt")
# file.close()
#append mode
# file = open('\\Users\\Susis\\PycharmProjects\\pythonProject\\python\\info.txt',"a")
# file.write("appnd")
# file.close()

with open('\\Users\\Susis\\PycharmProjects\\pythonProject\\python\\info.txt',"r") as file:
    print(file.read())
    print(file.tell())
    file.seek(0)
    print(file.tell())
    print(file.read())
