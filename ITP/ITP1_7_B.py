while 1:
    n,x=map(int,raw_input().split())
    conbi = 0
    if n == 0 and x == 0:
        break
    for i in range(1,n+1):
        for j in range(i+1,n+1):
            for k in range(j+1,n+1):
                if (i + j + k) == x:
                    conbi = conbi + 1
    print conbi
