# print(2+2)
# print(2-2)
# print(2*2)

a = True
b = True

if a and b:
    print("All true!") # This will print All True
if a or b:
    print("At least one is true!") # This will print At least one is true

a = True
b = False

if a and b:
    print("No Output!") # This will not print anything
if a or b:
    print("At least one is true!") # This will print At least one is true

a = False
b = False

if a or b:
    print("No Output") # This will not print anything
if not(a) and not(b):
    print("True") # This will  print 