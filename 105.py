#remove items
#note : you cannot remove items in a tuple.

#tuple are unchangable , so so you cannot remove items from it,
# but  yoy can use thesame work around as we usde for chsnging
#and addin tuple items:

#convert the tuple into a list, remove "apple",
# and convert it back into a tuple?

anju = ("unni", "chithu", "rema")
ashok = list(anju)
ashok.remove("unni")
anju= tuple(ashok)

print(anju)