import random

#從1-100中隨機讀取8個數字
nums = random.sample(range(1,100), 8)
print('origin data:',nums)
tmp = [0,0,0,0,0,0,0,0]

#將資料分成兩個部分:L(left)+R(right)
def merge(L, M, R):
    #left：目前左半部執行到第幾個element，L為初始值
    left = L
    #right：目前右半部執行到第幾個element，M+1為初始值
    right = M+1
    #i：merge後暫存tmp的索引值，L為初始值
    i = L
    while (left <= M) and (right <= R):
        if nums[left]<nums[right]:
            tmp[i]=nums[left]
            left = left+1
        else:
            tmp[i]=nums[right]
            right = right+1
        i = i+1
    while left <= M:
        tmp[i] = nums[left]
        i = i+1
        left = left +1
    while right <= R:
        tmp[i]=nums[right]
        i = i + 1
        right = right +1
    for i in range(L, R+1):
        nums[i]=tmp[i]

#Recursion
def mergesort(L,R):
    if L < R:
        M = (L+R)//2
        mergesort(L, M)
        mergesort(M+1, R)
        merge(L, M, R)
        print("\nL=",L,"M=",M,"R=",R,'\t',end='')
        for item in nums:
            print(item,' ',end='')

mergesort(0,7)
print()