import random

# 從1-100中不重複隨機產生9組數字
A = random.sample(range(1,100),9)
print('origin data:',A)

#外層變數i，控制內層變數j的上限
for i in range(len(A)-1,0,-1):
    for j in range(i):
        if A[j] > A[j+1]:
            #交換數字
            A[j],A[j+1] = A[j+1],A[j]
    print("\n氣泡排序外層迴圈執行第", 9-i,"次:")
    # print( )
    for item in A:
        print(item,' ',end="")
print()