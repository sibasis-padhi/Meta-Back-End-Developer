#global scope
global_list = [1,2,3,4,5]

# def add_to(item):
#     return global_list.append(item)
# add_to(6)

# print(global_list)

# def add_to(item):
#     return global_list.append(item)
    
# add_to(6)
# print(global_list)

# Above code is not pure function because it is modifying the global_list variable.

# Pure function
def add_to(item):
    global_list.append(item)
    return global_list
new_list = add_to(6)

print(global_list)
print(new_list)