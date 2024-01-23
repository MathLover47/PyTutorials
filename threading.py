from threading import *
list1 = []
list2 = []
def  start1(list1):
       for i in range(0,1000000):
              list1[i] = i%7
def start2(list2):
       for j in range(0,1000000):
              list2[j]= j**2

for i in range(0,2000000,2):
       list1.append(i)
for i in range(0,8000000,8):
       list2.append(i)
p1 = Thread(target=start1, name= "process1", args=(list1,))

p2 = Thread(target = start2, name = "process2", args=(list2,))
p1.start()
p2.start()

p1.join()
p2.join()




	
