a=1
while 1:
	l = map(int,raw_input().split())
	if l == [0,0]:
		break
	else :
		print ' '.join(map(str,sorted(l)))
		a += 1
