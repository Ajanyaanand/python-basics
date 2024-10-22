#update dictionary
#the update()method will update the dictionary
# with the items from the given arugument.


#the argument must be a dictinoary,
# or an iterable object with the key:value pairs.
# update the "year" of the car by using the uopdate() method:


thisdict = {
    "brand": "ford",
    "model": "mustang",
    "year": "1964",
}

thisdict.update({"year":2020})
print(thisdict)