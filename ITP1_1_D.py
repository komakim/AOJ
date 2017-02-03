S=input()
h,m,s=1,1,0.0
h=S/3600
m=(S-h*3600)/60
s=(S-h*3600-m*60) 
print ':'.join(map(str,[h,m,s]))