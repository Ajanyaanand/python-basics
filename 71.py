

#withoutlist comprehension
#you will have to write a for statement witha conditional test inside:

mylove = ["kuttu", "lalu", "adwt","kunjan", "vava"]
new = []

for x in mylove:
    if "a" in x:
        new.append(x)

print(new)




















#using list comprehension

mylove2 = ["va", "jj", "u", "j", "l"]

se2 = [x for x in mylove2 if "a" in x]

print(se2)