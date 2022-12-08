
##IN THIS PROJECT USER WILL ENTER SINGLE OR MULTIPLE NUMBERS AND YOUR SYSTEM WILL PREDICT THAT THE
##ENTERED NUMBER OR NUMBERS IS/ARE VALID NUMBERS IN A FIBONACCI SERIES OR NOT.

##.......................................MINI PROJECT  12 .....................................##

##userinput=map(int,input("ENTER THE NUMBER WITH SPACE SEPARATED: ").split(" "))
##c=0
##a=1
##b=1
##for i in userinput:
##    if i==0 or i==1:
##        print(f"{i}-Valid")
##    else:
##        while c<i:
##            c=a+b
##            b=a
##            a=c
##        if c==i:
##            print(f"{i}-valid")
##        else:
##            print(f"{i}-Invalid")


userinput=map(int,input("enter the number separated with space: ").split(" " ))
c=0
a=1
b=1
for i in userinput:
    if i==0 or i==1:
        print(f"{i}-valid")
    else:
        while c<i:
            c=a+b
            b=a
            a=c
        if c==i:
            print(f"{i}-valid")
        else:
            print(f"{i}-Invalid")




