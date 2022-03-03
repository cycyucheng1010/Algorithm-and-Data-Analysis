# 排序
## 常見的排序演算法
* 氣泡排序法(Bubble Sort)
* 選擇排序法(Selection Sort)
* 插入排序法(Insertion Sort)
* 合併排序法(Merge Sort)
* 快速排序法(Quick Sort)
* 堆積排序法(Heap Sort)
### Bubble sort
* 跟所有自己右邊的值比大小，若右邊的值比自己大就不換，反之則換
* 第一個做n-1次，第二個做n-2次以此類推....
* 共做n^2/2次

![image](https://user-images.githubusercontent.com/62127656/156571274-9bb01c17-0106-4201-a545-69249874e99a.png)


```python
import random

# 從1-100中不重複隨機產生9組數字
A = random.sample(range(1,100),9)
# print(A)

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
```
### slection sort
* 原本的原理是選擇最小的加入的隔離區中，後在程式碼中常用的方法為搜尋最大之值並將其交換到最右邊

![image](https://user-images.githubusercontent.com/62127656/156571023-fb61a055-7f45-4b67-ba46-011d9ddb65bc.png)


```python
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
```
### insertion sort
* 插入排序是從數列的左邊開始，往右往右依次排序下去。過程中，左邊的數一一完成排序，右邊剩下尚未確認的數。在右邊尚未搜尋的領域中取出一個數，插入已排序完成的領域中的適當位置。

![image](https://user-images.githubusercontent.com/62127656/156571131-544d499f-24a3-4c71-bd22-eb7a99fe32eb.png)


```python
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
```
