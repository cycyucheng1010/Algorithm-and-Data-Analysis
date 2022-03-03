import random

#從1-100中隨機讀取8個數字
nums = random.sample(range(1,100), 8)
print('orgin data:',nums)


def quicksort(L, R):
    #當L<R表示還有兩個以上的元素需要排列
    if(L < R):
        #i初始化變數為L
        i=L
        #j初始化變數為R+1
        j=R+1
        while(1):
            #變數i不斷遞增直到找出nums[i]>nums[L]的元素，或i>R就停止
            i=i+1
            while((i < R) and (nums[i] < nums[L])):
                i=i+1
            #變數j不斷遞減直到找出nums[j]<nums[L]的元素，或j小於L就停止
            j=j-1
            while((j>L) and (nums[j]>nums[L])):
                j=j-1
            #當i>=j就停止迴圈
            if(i >= j):break
            nums[i],nums[j] = nums[j], nums[i]   
        nums[L],nums[j] = nums[j],nums[L]
        print("\nL=", L, " j=", j, " R=", R,'\n')
        for item in nums:
            print(item, ' ',end='')
        quicksort(L, j-1)
        quicksort(j+1, R)

for item in nums:
    print(item, ' ',end='')
quicksort(0,7)
print()