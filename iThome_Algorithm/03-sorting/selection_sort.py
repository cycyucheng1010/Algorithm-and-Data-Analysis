import random

# 從1-100中不重複隨機產生9組數字
nums = random.sample(range(1,100),9)

print('origin data:',nums)

# i控制j的上限值
for i in range(8, 0, -1):
    #初始化變數0
    max = 0
    for j in range(1, i+1):
        if nums[j] > nums[max]:
            max = j
    nums[i], nums[max] = nums[max], nums[i]
    print("\n選擇排序的執行結果:",9-i,"次")
    for item in nums:
        print(item,' ',end="")
print()

