dict1 = {'0':"Zero",'1':"One",'2':"Two",'3':"Three",'4':"Four", '5':"Five",'6':"Six",'7':"Seven",'8':"Eight" , '9': "Nine"}
num = str(input("Enter phone number"))
str1 = ""
'''for i in range(len(num)):

    str1 += dict1[num[i]]
'''
for i in num:
    str1 += dict1[i]
print(str1)