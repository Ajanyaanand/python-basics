#add a new item to the orginal dictionary.
#and see that the key list gets updated as well?

car = {
    "brand": "ford",
    "model": "mudsang",
    "year": 293
}
x = car.keys()
print(x) #before the change

car["color"] = "white"
print(x) #after the change