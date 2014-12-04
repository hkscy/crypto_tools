# Performs the Euclidean algorithm given a pair of values a and b.
#
# Euclid's algorithm is a method of finding the greatest common denominator (GCD) of two
# integers a and b. This algorithm works by iteratively dividing the larger integer by the
# smaller integer, stopping when the remainder of division is 0. The GCD is the last non-zero
# remainder.
#
# Christopher Hicks : 4/12/14

print 'This program uses Euclid\'s algorithm to find the gcd of two integers.'
a = aa = raw_input('Enter the first positive integer: ')
a = int(a)
b = bb = raw_input('Enter the second positive integer: ')
b = int(b)

if a > b: 		
	a,b = b,a # Ensure that a is smaller than b

cont = True
while cont: # Emulate a do-while loop.
	divisor = b/a
	remainder = b%a
	if remainder == 0: # The gcd is the last non-zero remainder.
		cont = False
	else:
		b = a # The previously smallest value becomes the largest.
		a = remainder # The smallest values becomes the remainder of the last division.
print 'GCD({},{}) = {}.'.format(aa,bb,a)
