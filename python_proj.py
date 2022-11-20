print("Program to find leap year")

a = (input("Enter initial date(in ddmmyyyy format): "))
b = (input("Enter final date(in ddmmyyyy format): "))

y1 = int(a[-4:])
y2 = int(b[-4:])

def leap(y1,y2):
    print("\nAll leap years between {} to {} are".format(y1,y2))
    for x in range(y1,y2):
        if( x%400==0):
            print(x)
        elif(x%100!=0 and x%4==0):
            print(x)

if(y1>y2):
    print("\nFinal date can't be greater than initial date")
    exit()
else:
    leap(y1,y2)


