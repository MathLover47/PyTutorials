l1 = [5,4,9,0,1,10,3,2,1,20,1,2,1,4,5,10,1,1]
l2 = l1.copy()
l2.remove(1)
print(l2)
l1.pop()
print(l1)
l1.remove(10)
print(l1)
l1.clear()
print(l1)
l2.append(30)
print(l2)
print(l2.index(10))
print(l2.index(10,5))
print( 30 in l2)
print(l2.count(1))
l2.insert(5,100)
print(l2)
print(len(l2)
      )




#l3 = l2.copy()
# l4 = l3.copy()
'''for i1 in range(20):
    for i2 in range(i1+1,20):
        if l3[i1] == l4[i2]:
l2.remove(i2)'''
'''index1 = 0
index2 = 1
while index1 < len(l2):
    while index2 < len(l2):
        if l2[index1] == l2[index2]:
            l2.remove(l2[index2])
        index2 += 1
    index1 += 1
'''

print(l2)
uniques = []
for number in l2:
    if number not in uniques:
        uniques.append(number)
print(uniques)
l2.sort()
print(l2)
l2.reverse()
print(l2)
