def repSqAlg(g, x):
	y = g
	z = 1
	x_bckw = bin(x)[2::][::-1]
	print "g = " + str(g)
	print "x = " + x_bckw

	for i in range(0, len(x_bckw)):
		if(x_bckw[i] == '1'):
			z = z*y
		y = pow(y,2)
		print "y = " + str(y) + " z = " + str(z)

	return z

print "5^53 = " + str(repSqAlg(5,53))
