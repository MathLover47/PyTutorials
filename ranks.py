
x = (int(input("Enter number of rank: ")))
list1 = ['A','B','C','D','E','F']
if (x <= 6) and ( x >= 0):
    print(list1[x-1])
else:
    print("Illegitimate choice can't be more than 6 or less than a zero")
