
#local variables

def aju():
 z = "fantastic"
 #z is an local variable,can be acessed only inside function.
 print(z)

aju()


#global keyword
def aju():
    global x
    x = "fantastic"

aju()
print("python is" +x)