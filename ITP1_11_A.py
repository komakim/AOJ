d = map(int,raw_input().split())
#m = {"E":[4,2,1,6,5,3],"N":[2,6,3,4,1,5],"W":[3,2,6,1,5,4],"S":[5,1,3,4,6,2]}
m = {"E":[3,1,0,5,4,2],"N":[1,5,2,3,0,4],"W":[2,1,5,0,4,3],"S":[4,0,2,3,5,1]}

nd = [0]*6
for x in raw_input():
    for j in range(6):
        nd[j] = d[m[x][j]]
    d = list(nd)
print d[0]
