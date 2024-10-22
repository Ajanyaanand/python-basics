#make chamge inthe original dictionary,
# and see the values list gets updated as well:


car = {
    "brand": "ford",
    "model": "mustang",
    "year": 129
}

x = car.values()
print(x) # before the change

car["year"] = 348
print(x) # after the change