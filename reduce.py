from functools import reduce
lst = [1,2,3,4,5]
def mul(x,y):
	return x*y
prod = reduce(mul,lst)
print(prod)
