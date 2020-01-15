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


lambda num :  num** 2

print(map(lambda num :  num** 2, my_nums))

#print(square(10))
print(names)

print(map(lambda name:name[0], names))


## Write a function that computes the volume of a sphere given itsradius. 

def vol(rad):
	return (4.0/3)*(3.14)*(rad**3)

####################

## Write a function that checks whether a number is in a given range(inclusive of highh and low)

def ran_check(num, low, high):
	#Check if num is between low and high(including low and high)
	if num in range(low, high):
		print " %s is in the range" %str(num)
	else:
		print "THe number is outside of range"

ran_check(10,8,20)



#### FUnction that acceps a string and caclculates how many upper and lower case letter it has.

def up_low(s):
	d={"upper":0, "lower":0}
	for c in s:
		if c.isupper():
			d["upper"] +=1
		elif c.islower():
			d["lower"] +=1
		else:
			pass

	print("Original String : ", s)
	print("No. of Upper case characters: ", d["upper"])
	print("No. of Lower case characters: ", d["lower"])

s = "Hello Mr. Rogers, how are you This fine Tuesday?"

up_low(s)





























