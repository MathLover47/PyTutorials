Python 3.8.7 (tags/v3.8.7:6503f05, Dec 21 2020, 17:59:51) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> 
>>> print("hello")
hello
>>> a = [
	[1,2,3],
	[4,5,6],
	[7,8,9]
	]
>>> print(a)
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> for row in a
SyntaxError: invalid syntax
>>> for row in a:
	for col in row
	
SyntaxError: invalid syntax
>>> for row in a:
	for col in row:
		print(col)

1
2
3
4
5
6
7
8
9
>>> 