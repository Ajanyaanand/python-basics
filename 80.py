#coustomize sort function

#you can also customize yourown function by
# using the keywoed arugment key = function.
#thefunction will return
# a numberthat will be used to sort the list (the lowest number first)

#soet the list based on how close the number is to 50?

def myfunc(n):
    return (n - 50)

thislist = [100, 50, 65, 82, 23]

thislist.sort(key = myfunc )
print(thislist)


#myf