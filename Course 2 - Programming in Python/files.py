# with open('newfile.txt', mode='w') as file:
#     file.write('This is a new file created by Python.')

# with open('newfile.txt', mode='w') as file:
#     file.writelines(["This is a new file created by Python.","\nThis is another line to be added to the file."])

try:
    with open('demo/newfile.txt','a') as file:
        file.writelines(["This is a new file created by Python.","\nThis is another line to be added to the file."])
except FileNotFoundError as err:
    print('File not found')
    raise err