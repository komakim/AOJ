import sys
def reviewRe():
    #print ' '.join(map(str,map(str,residence[i][j])))
    for area in range(4):
        for floor in range(3):
            print area ,floor
            print ''.join(map(str,residence[area][floor][:]))
        print "###################"


if __name__ == '__main__':
    residence = [[[0 for room in range(10)] for floor in range(3)] for area in range(4)]
    print residence
    reviewRe()
    #n = input()
    #for i in range(n):
    #    b,f,r,v = map(int,raw_input().split())
    #for i in range(area) :
    #    residence [i]
