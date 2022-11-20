print("Program to find leap year")

a = (input("Enter initial date(in dd/mm/yyyy format): "))
b = (input("Enter final date(in dd/mm/yyyy format): "))

y1 = int(a[-4:])
y2 = int(b[-4:])

def leap(y1,y2):
    print("\nAll leap years between {} to {} are".format(y1,y2))
    for x in range(y1,y2):
        if( x%400==0):
            print(x,end=(", "))
        elif(x%100!=0 and x%4==0):
            print(x,end=(", "))
def notleap(y1,y2):
    print("\nAll non leap years between {} to {} are:".format(y1,y2))
    for x in range(y1,y2):
        if( x%100==0 and x%400!=0):
            print(x,end=(", "))
        elif(x%100!=0 and x%4!=0):
            print(x,end=(", "))
if(y1>y2):
    print("\nFinal date can't be greater than initial date")
    exit()
else:
    leap(y1,y2)
    print("")
    notleap(y1,y2)


