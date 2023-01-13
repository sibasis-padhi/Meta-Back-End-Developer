# def devide_by(a,b):
#     return a/b
# print(int(devide_by(40,4)))

# def devide_by(a,b):
#     try:
#         return a/b
#     except ZeroDivisionError as e:
#         print(e)
#         return None
# print(int(devide_by(40,0)))

def devide_by(a,b):
    return a/b
try:
    ans = devide_by(40,0)
except Exception as e:
    print("Something went wrong!",e)
