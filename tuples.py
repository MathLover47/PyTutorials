Python 3.8.7 (tags/v3.8.7:6503f05, Dec 21 2020, 17:59:51) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> tuple1 = (4,2,5)
>>> print(tuple1.count )
<built-in method count of tuple object at 0x0000027147673B40>
>>> print(typle1.count())
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print(typle1.count())
NameError: name 'typle1' is not defined
>>> print(tuple1.count())
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print(tuple1.count())
TypeError: count() takes exactly one argument (0 given)
>>> print(tuple1[1])
2
>>> tuple1[0] = 3
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    tuple1[0] = 3
TypeError: 'tuple' object does not support item assignment
>>> tuple2 = (     (1,2), (3,5), (5,5) )
>>> for item in tuple2:
	for i in item:
		print(i)
	print("_____________________")

1
2
_____________________
3
5
_____________________
5
5
_____________________
>>> 