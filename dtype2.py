Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 10
>>> print(type(a))
<class 'int'>
>>> a,b=20,30
>>>  print(type(a),type(b))
...  
SyntaxError: unexpected indent
>>> print(type(a),type(b))
<class 'int'> <class 'int'>
>>> a = 20.5
>>> print(type(a))
<class 'float'>
>>> print(2+2*10/5)
6.0
>>> print(((2+2)*10)/5)
8.0
>>> print((2+2*10)/5)
4.4
>>> a = 1+2j
>>> print(a)
(1+2j)
>>> type(a)
<class 'complex'>
>>> isinstance(a, complex)
True
>>> a = 5j
>>> print(a)
5j
>>> a = 2 + 0j
>>> print(a)
(2+0j)
>>> type(a)
<class 'complex'>
>>> a = 10 + 5j
>>> print(a,"\tis of type:\t",type(a))
(10+5j) 	is of type:	 <class 'complex'>
