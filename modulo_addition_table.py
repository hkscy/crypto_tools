# This program calculates a table of additions in modulo n
# Addition in modular arithmetic is "arithmetic on the face of a clock."
# Christopher Hicks : 4/12/14
class colour: # Used for formatting text output via print.
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'
  END = '\033[0m'

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
		print repr((i+j)%n).rjust(3), # Ensure addition is modulo n
	print
