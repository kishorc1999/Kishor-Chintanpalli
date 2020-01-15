"""function with default argument"""
"""Assingnment of 0 shuld be left to right"""
def fun(a=0,b=0,c=0):
	print a
	print b
	print c
fun()
fun(10)
fun(10,20)
fun(10,20,30)