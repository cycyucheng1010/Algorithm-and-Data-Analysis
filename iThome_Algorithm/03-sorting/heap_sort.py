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