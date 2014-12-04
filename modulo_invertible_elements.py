# This program calculates a table of multiplications in modulo n
# Multiplication in modular arithmetic is done a*b(mod n)
# Invertible elements are identified where the product of a number and at least one other is 1.
# Christopher Hicks : 4/12/14
class colour: # Used for formatting text output via print.
	BOLD = '\033[1m'
   	UNDERLINE = '\033[4m'
   	END = '\033[0m'

invertible_elements = [] # Init. a list for holding group of invertible elements.

n = raw_input(colour.BOLD + "Enter the value of n: ")
n = int(n)

# Print out the column headings at the top.
print '#'.rjust(3),
for i in range(n):
	print repr(i).rjust(3),
print colour.END

# Print out the row headings and table data.
for i in range(n):
	# Justify to the right of a two character width column
	print colour.BOLD + repr(i).rjust(3) + colour.END, 
	for j in range(n):
		m = (i*j)%n
		print str(m).rjust(3), # Ensure addition is modulo n
		if m == 1: # Is invertible if product with at least one other is 1
			invertible_elements.append(j)
	print
print 'The list of invertible elements in modulo ' + str(n) + ' is:'
print invertible_elements
