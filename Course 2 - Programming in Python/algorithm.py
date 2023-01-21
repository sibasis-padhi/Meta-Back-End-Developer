#Algorithm for a palindrome

str = 'racecar'

# print(str[0])
# print(str[6])

# [0] == [6]
# [1] == [5]
# [2] == [4]
# Need to check if these conditions are true or false

# def is_palindrome(str):
#     startIndex = 0
#     endIndex = len(str) - 1

#     for x in str:
#         if str[startIndex] != str[endIndex]:
#             return False
#     return True
# print(is_palindrome(str))

def is_palindrome(str):
    for i in range(len(str)):
        if str[i] != str[len(str)-1-i]:
            return False
    return True
print(is_palindrome(str))