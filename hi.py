 def add(x,y):
     z=x+y
     return z
 def sub(x,y):
     z=x-y
     return z



 while True:
     a=int(input("enter the a value : "))
     b=int(input("enter the b value : "))
     c=add(a,b)
     f=sub(a,b)
     print("your add value : {}".format(c))    
     print("your sub value : {}".format(f))

     a=input("if you want to continue press yes otherwise no : ")
     if a=="yes":
         continue
     else:
         break



def hello():
    a="hi hello how are you"
    return a


h=hello()
if "how are you" in h:
    print("helo")

















