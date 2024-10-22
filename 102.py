#update tuple

#change tuple values
#once a tuple is created, you cannot change its values.
#tuples areunchangable, or immutable as it also is called.

# you can convert the tupleinto a list,
# change the list, and convert the list back into a tuple.

#convert the tuple into a list to be able to cahnge it?

ammu = ("appu", "ammus", "manu")
anu = list(ammu)
anu[1] = "malu"
ammu = tuple(anu)

print(ammu)