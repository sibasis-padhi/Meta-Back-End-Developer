# file = open('test.txt', mode='r')
# data = file.readline()
# print(data)
# file.close()

with open('newfile.txt', mode='r') as file:
    data = file.readline()
    print(data)