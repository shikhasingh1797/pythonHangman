catA=int(input("enter catA="))
catB=int(input("enter catB="))
mouse=int(input("enter mouse"))
a=abs(catA-mouse)
b=abs(catB-mouse)
if a<b:
    print("catA")
elif a>b:
    print("catB")
else:
    print("mouse")