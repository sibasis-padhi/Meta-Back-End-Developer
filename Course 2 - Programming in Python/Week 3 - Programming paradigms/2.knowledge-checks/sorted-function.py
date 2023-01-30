coffees = ['Espresso', 'Cappuccino', 'Café au lait', 'Café mélange', 'Café mocha', 'Café latte']
# print(sorted(coffees))

# def reverse_sort(coffees):
#     return sorted(coffees, reverse=True)
# print(reverse_sort(coffees))

def reverse(coffees):
    return coffees[::-1]
reversed_coffees = map(reverse, coffees)

for x in reversed_coffees:
    print(x)
