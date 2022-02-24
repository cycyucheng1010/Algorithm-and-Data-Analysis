#選擇排序

def showdata():
    for i in range(8):
        print('%3d'%data[i],end='')
    print()

def select(data):
    for i in range(7):
        for j in range(i+1,8):
            if data[i]>data[j]:
                temp = data[i]
                data[i]=data[j]
                data[j]=temp
    print()

data = [16,25,39,27,12,8,45,63]
print('orgin data:')
showdata()
select(data)
print('result:')
showdata()