set_a = {1,2,3,4,5}
set_b = {1,2,3,4,5,5}
set_c = {4,5,6,7,8}

# print(set_a)
# print(set_b)

# set_a.add(6)
# print(set_a)

# set_a.remove(4)
# print(set_a)

# set_a.discard(2)
# print(set_a)

print(set_a.union(set_c))
print(set_a | set_c)
print(set_a.intersection(set_c))
print(set_a & set_c)
print(set_a.difference(set_c))
print(set_a - set_c)

print(set_a.symmetric_difference(set_c))
print(set_a ^ set_c)