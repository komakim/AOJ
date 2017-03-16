import sys
while 1:
	H,W=map(int,raw_input().split())
	if H==0 and W==0:
		break;
	else:
		for x in range(H):
			for y in range(W):
				if (x + y)% 2: 
				sys.stdout.write('#')
			else:
				sys.stdout.write('.')

			sys.stdout.write('\n')
	sys.stdout.write('\n')