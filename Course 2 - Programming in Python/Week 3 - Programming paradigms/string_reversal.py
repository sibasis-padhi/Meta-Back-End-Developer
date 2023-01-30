# str[start:stop:step]
#using slicing
# trial = "reversal"
# new_trial = trial[::-1]
# print(new_trial)

#using Recursion
def string_reversal(string):
    if len(string) == 0:
        return string
    else:
        return string_reversal(string[1:]) + string[0]
string = "reversal"
reverse = string_reversal(string)
print(reverse)