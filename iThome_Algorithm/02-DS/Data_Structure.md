# Data Structure
* 資料結構是可以有效改善記憶體使用效率的方法之一
* 有以下幾種排序方式:
   * 列表(List)
   * 陣列(Array)
   * 堆疊(Stack)
   * 佇列(queue)
   * 雜湊表(Hash Table)
   * 堆積(Heap)
   * 二元搜尋數(binary search tree)
## List
* 分為有序跟無序
* 利用線性搜尋的方式進行
* Big O = O(n)
## Array 
* 是一種儲存資料的方式
* 相較於列表更容易存取
* 但新增或刪除數據時較麻煩
* 與列表相同之處:
   * 兩者的資料結構是可變的
   * 可以切片或迭代
   * 都有索引
   * 可用於儲存資料
* 與列表不同之處:
   * 列表可放不同資料形態，陣列僅能放相同資料形態

## Stack
* 堆疊是一種後進先出(Last In First Out)(LIFO)的資料結構
* 根據堆疊後進先出的特性，進行兩種的操作：
   * push：將資料放入堆疊頂端
   * pop：將堆疊頂端資料移除

## queue
* 佇列是一種先進先出的資料結構(FIFO, First-In-First-Out)
* 根據佇列先進先出的特性，進行兩種操作
   * enqueue：由最後端添加資料
   * dequeue：由最前端刪除資料
## Hash Table
* Hash這個詞在電腦科學中很常見，將一組值轉換成另一組，是一種加密技術。
* 若hash後有兩組資料位置相同，此時產生的情況稱為Collision。
### 一般常見的Hash Function有兩種: Dicision method and Multiplication Method
* Divisiion method
   * 優點:速度快
   * 缺點: 使用2的次方進行運算容易出現衝突現象
   * 公式: ```index = key mod m```
* Multiplication method
   * 公式: ```index = [m(keyA%1)]```
   * A是無理數
   * mod1將整數去除，得到0<p<1
* 透過實作可發現文字每次hash後的值都不同，相反的數字則維持   
```python
x = hash("a")
print(x) #963309178111316638
y = hash(8823748)
print(y) #8823748
z = hash(str([1,2,3]))
print(z) #6529461775645613167
```
## Binary tree
* 二元樹可以為空集合
* 每 1 個節點最多只有 2 個子節點，左節點與右節點
* 有次序關係，左節點會排在右節點之前，不能顛倒
### Complete Tree
* 一個高度為 h ，節點數量小2^h-1例如：一個高度(Height)為 3 的二元樹，節點小於 7 個
由上到下，由左至右都跟完滿二元樹一一對應
![image](https://user-images.githubusercontent.com/62127656/156524328-86f5469d-c053-46c5-b06b-c2857133e9bb.png)

### Full Tree
* 最後一層的節點數為0 or 2

![image](https://user-images.githubusercontent.com/62127656/156524345-e85bcd03-c570-4000-bb82-e7319df622c2.png)

## Heap
* 根據大小進行排序並可表示成array型式，可參考下圖
![image](https://user-images.githubusercontent.com/62127656/156524787-cbfaab78-5749-4feb-bc30-3e02ec5be44a.png)
