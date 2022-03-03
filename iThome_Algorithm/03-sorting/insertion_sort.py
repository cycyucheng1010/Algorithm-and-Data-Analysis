import random

#從1-100中隨機讀取9個數字
nums = random.sample(range(1,100), 9)
print('orgin data:',nums)

# i控制j的上限值
for i in range(1, 9):
    #初始化變數nums[i]
    insert = nums[i]
    j = i-1
    #內層迴圈從i-1到0，每次遞減1
    while j>=0:
        if insert < nums[j]:
            nums[j+1]=nums[j]
        else:
            break 
        j = j-1
    #將變數insert儲存到nums[j+1]
    nums[j+1]=insert
    print("\n插入排序執行次數為：", i ,"次")
    for item in nums:
        print(item,' ',end="")
print()