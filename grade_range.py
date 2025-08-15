x = 1
while x > 0:
    print("Enter grade in percent(number <=0 to exit:")
    x = int(input())
    if x > 100:
        print("error, can't be more than 100")
    elif x >= 94 :
        print("A+*")
    elif x >= 91:
        print("A+")
    elif x >= 88:
        print("A")
    elif x >= 85:
        print("A-")
    elif x >= 82:
        print("B+")
    elif x >= 79:
         print("B")
    elif x >= 76:
        print("B-")
    elif x >= 73:
        print("C+")
    elif x >= 70:
        print("C")
    elif x >= 67:
        print("D")
    elif x >= 55:
        print("F")
    else:
        print("Failed Grade")

    
    
    
