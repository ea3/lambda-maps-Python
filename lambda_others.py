def square(num):
	return num**2

my_nums = [1,2,3,4,5]

print(map(square,my_nums))


def splicer(mystring):
	if len(mystring) % 2 == 0:
		return 'EVEN'

	else:
		return mystring[0]


names = ['Andy', 'Eve', 'Sally']

print (map(splicer, names))

