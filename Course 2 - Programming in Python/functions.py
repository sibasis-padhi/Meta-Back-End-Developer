# bill = 175.00
# tax_rate = 15
# total_tax = (bill * tax_rate) / 100

# print("The total tax is: " + str(total_tax))

def calculate_tax(bill, tax_rate):
    total_tax = (bill * tax_rate) / 100
    return total_tax

print("The total tax is: " + str(calculate_tax(175, 15)))