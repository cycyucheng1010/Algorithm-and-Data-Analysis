#泡沫排序
data = [16,25,39,27,12,8,45,63]
print("origin data :")
for i in range(0,(len(data)-1)):
    print('%3d'%data[i],end='')
print('\n')

for i in range(7,-1,-1): 
    for j in range(i):
        if data[j]>data[j+1]:
            temp = data[j+1]
            data[j+1]= data[j]
            data[j] = temp
    print('%d次排序'%(8-i),end='')

    for j in range(8):
        print('%3d'%data[j],end='')
    print()

print('result:')
for j in range(8):
    print('%3d'%data[j],end='')
print('\n')
