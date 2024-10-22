#you can use the index number {0}
#tobe sure the arguments are placed inthe correct place holders:


quanity = 3
itemno = 567
price = 49.95
myorder = "i want to pay {2} dollars for {0} pieces of item {1}"

print(myorder.format(quanity, itemno,price))