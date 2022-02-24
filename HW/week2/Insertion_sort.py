def showdata():
    for i in range(8):
        print('%3d'%data[i],end='')
    print()

def insert(data):
    n = len(data)
    for i in range(n-1):
        key = data[i+1]
        j = i
        while j >=0 and key < data[j] :
                data[j+1] = data[j]
                j -= 1
        data[j+1] = key

data = [16,25,39,27,12,8,45,63]
print('origin data:')
showdata()
insert(data)
print('result:')
showdata()
