import random
list1 = list(range(20))
for i in range(20):
    list1[i] = random.random()
max = 0
for item in list1:
    if item > max:
        max = item
        
print(list1)
print(max)