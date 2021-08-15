Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def findArea(r);
SyntaxError: invalid syntax
>>> def findArea(r):
	PI=3.14
	return PI * ( r*r );

>>> print("Area of circle = %.6f" % findArea(6));
Area of circle = 113.040000
>>> 