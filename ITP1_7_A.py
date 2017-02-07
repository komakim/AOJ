while 1:
    m,f,r=map(int,raw_input().split())
    #m:Midterm exam  f:final exam r:Retest
    score=m+f
    if m == -1  or  f ==  -1 :
        if m == -1 and f == -1 and r == -1 :
            break
        else: print 'F'
    elif score >= 80:
        print 'A'
    elif score >= 65:
        print 'B'
    elif score >= 50 or (score >= 30 and r >= 50):
        print 'C'
    elif score >= 30:
        print 'D'
    else:
        print 'F'
