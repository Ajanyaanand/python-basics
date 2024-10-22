# add a new item to the orginal dictionary,
# and see the values list gets updated as well:

car = {
    "brand": "ford",
    "model": "mustang",
    "year": 367
}

x = car.values()
print(x)  #before the change

car["color"] = "red"
print(x) # after the change