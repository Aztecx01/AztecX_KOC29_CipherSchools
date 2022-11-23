print("Program to find leap year")

a = (input("Enter initial date(in dd/mm/yyyy format): "))
b = (input("Enter final date(in dd/mm/yyyy format): "))

y1 = int(a[-4:])
y2 = int(b[-4:])
a = []
b = []

def leap(y1,y2):
    for x in range(y1,y2+1):
        if( x%400==0):
            a.append(x)
        elif(x%100!=0 and x%4==0):
            a.append(x)
        else:
            b.append(x)
    return a,b

if(y1>y2):
    print("\nFinal date can't be greater than initial date")
    exit()
else:
    leap(y1,y2)
    print("\nAll leap years between {} to {} are".format(y1,y2))
    print(a)
    print("\nAll non-leap years between {} to {} are".format(y1,y2))
    print(b)


