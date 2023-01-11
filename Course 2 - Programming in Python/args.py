# def sum_of(a,b):
#     return a+b
# print(sum_of(1,2))
# print(sum_of(1,2,3)) #TypeError: sum_of() takes 2 positional arguments but 3 were given

def sum_of(*args):
    sum = 0
    for x in args:
        sum += x
    return sum
print(sum_of(1,2,3,4))
