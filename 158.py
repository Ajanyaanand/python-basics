# add a nwe item to the original dictionary,
#and see that the items list gets updated as well:

car = {
    "brand": "ford",
    "model": "mustang",
    "year": 2020
}
x = car.items()
print(x)

car["color"] = "red"
print(x)