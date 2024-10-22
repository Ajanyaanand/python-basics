#performe a case - insensitive sort of the the list:

thislist = ["banana," "Banana", "orange", "kiwi","cherry", "apple1", "apple"]

thislist.sort(key = str.lower)

print(thislist)

#the key parameter is set to str.lower,
# whic means that the list will be orted based
# on the lowercase versionof each string element.

#"banana".lower()returns "bana

