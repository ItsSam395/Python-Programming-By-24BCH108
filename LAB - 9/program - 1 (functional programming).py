def fun():
    print("Function fun() is called.")

def disp():
    print("Function disp() is called.")

def msg():
    print("Function msg() is called.")

lst=[fun, disp, msg]

for function in lst:
    function()
