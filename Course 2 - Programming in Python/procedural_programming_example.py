def bill_total(bill):
    total=0.00
    for k,v in bill.items():
        total += v
    return total

def calculate_tax(percent,bill_total):
    return round((percent*bill_total)/100.0,2)

Food_bill = {
    1:3.99,
    2:2.99,
    3:11.99,
    4:22.99,
    5:1.99,
}

food_total = bill_total(Food_bill)
tax_total = calculate_tax(15,food_total)

print("Food total: $",food_total+tax_total)