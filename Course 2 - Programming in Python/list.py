list=[1,2,3,4,5]
# list1=["a","b","c","d","e"]
# list2=["Hello",1,True,2.5]
# list3=[1,[2,3],4]
 
print(*list)
print(list)

list.insert(len(list),6)
print(list,sep=" ")

list.append(7)
print(list,sep=" ")

list.extend([8,9,10])
print(list,sep=" ")

list.pop(3)
print(list,sep=" ")

list.remove(1)
print(list,sep=" ")

for x in list:
    print(x,end=" ")