# 疊代法
sum =1
n = int(input('n=?'))
for i in range(0,n+1):
    for j in range(i,0,-1):
        sum = sum* j
    print('%d!=%3d'%(i,sum))
    sum=1


