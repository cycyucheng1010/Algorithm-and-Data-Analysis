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
### Slection sort
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
### Insertion sort
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
### Merge Sort
* Divide and conquer（分而治之法）
* 將一個無序的資料結構，排序為從大到小的array。先將array從中間切割，再將切割後的資料進行切割，直到兩兩進行比對，比對後進行由右到左，由小到大的排序，最後再將排序後的資料進行組合。
* 更有效率的演算法（所耗費的時間複雜度為n log(n))
* 並行性

![image](https://user-images.githubusercontent.com/62127656/156573717-11abb6db-2252-4dda-81b8-f47ec48e90dc.png)

```python 
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
```
### Quick sort
* 從數列中隨機選擇一個數作為基準(Pivot)，接著將剩下的數字分為比Pivot小或比Pivot大的值。

![image](https://user-images.githubusercontent.com/62127656/156574034-f2893c34-9d0b-48e2-aa6c-05798df5dc18.png)

```python
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
```
<<<<<<< HEAD
=======
### Heap sort
* 堆積排序最初要將n個數儲存到堆積中的時間是O(n log(n))
* 與氣泡排序、選擇排序、插入結構相比，堆積排序處理速度較快，但也因為這種複雜的資料結構，建置與維護變得複雜。
```python
import random

#從1-100中隨機讀取8個數字
nums = random.sample(range(1,100), 9)
print(nums)

def max_heapify(h, n, x):
    #如果(2*x+1) <= n，表示有右子節點
    if (2*x+1) <= n :
        #如果h[2*x] > h[2*x+1]，表示左子節點大於右子節點
        if h[2*x] > h[2*x+1]:
            max = 2*x
        else:
            max = 2*x+1
    else:
        max = 2*x
    #如果h[x]<h[max]，則兩個子節點互換
    if h[x] < h[max]:
        h[x], h[max] = h[max], h[x]
        #如果2*max<=n，表示h[max]也有子節點，recursion max_heapify是否與孫節點互換
        if 2*max <= n:
            max_heapify(h, n, max)

#將任何陣列轉換為Max Heap
def build_max_heap(h, n):
    #迴圈變數
    for i in range(n//2, 0, -1):
        max_heapify(h, n, i)

def heap_sort(h, n):
    build_max_heap(h, len(h)-1)
    print(h)
    for i in range(n, 1, -1):
        h[i], h[1] = h[1], h[i]
        if i > 2:
            max_heapify(h, i-1, 1)
        print(h)

heap_sort(nums, len(nums)-1)
print(nums)
```
## 結論
![image](https://user-images.githubusercontent.com/62127656/158753212-4b551d4e-24bb-4846-b6e4-7861808aab17.png)
>>>>>>> b61eb8e450496d51e5f562863f2fb7f62836f03a
