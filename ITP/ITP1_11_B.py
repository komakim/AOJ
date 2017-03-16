d = map(int,raw_input().split())
num = int(input())
roll = [[1,2,4,3],[5,2,0,3],[1,5,4,0],[1,0,4,5],[0,2,5,3],[4,2,1,3]]
for i in range(num) :
        t,f = map(int,raw_input().split())
        tt = roll.index(t)
        tf = roll.index(f)
        tf = table[tt].index(tf) + 1
        if tf > 3 : tf = 0
        print roll[roll[tt][tf]]
