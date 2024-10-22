#33make a changein the original dictinory,
#and see that the items list getsupdated as well


car = {
    "brand": "ford",
    "model": "mustang",
    "year": 2020
}
x = car.items()
print(x)

car["year"] = 2024
print(x)