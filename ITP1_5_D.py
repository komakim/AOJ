import sys
try:
	while 1:
		N=input()
		i = 1
		while 1:
			if (i % 3) == 0 :
				sys.stdout.write(" ")
				sys.stdout.write("%d" % i)
			else:
				if (i % 10 ) == 3 :
					sys.stdout.write(' ')
					sys.stdout.write("%d" % i)
				else:
					if  (i/10)%10 == 3:
						print (i/10)%10,"a"
						sys.stdout.write(' ')
						sys.stdout.write("%d" % i)
			if i+1  >  N:
				sys.stdout.write('\n')
				raise Exception
			i += 1
except Exception:
	pass