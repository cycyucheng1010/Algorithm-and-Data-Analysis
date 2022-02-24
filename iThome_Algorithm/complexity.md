## 時間複雜度 Time complexity
* 時間指的不是程式執行時所計算的秒數，而是從程式執行的第一步到完成，中間的步數。

![image](https://user-images.githubusercontent.com/62127656/155477285-5f35ef9f-fcf5-4369-9058-1200ffe87877.png)

* O(1)：陣列讀取
* O(n)：無序陣列的搜尋
* O(log n)：二分搜尋
* O(n log n)：合併排序，最快的比較排序
* O(n²)：泡沫排序、插入排序
* O(2^n)：費波那契數列

## 空間複雜度 Space Complexity
* 空間指的是在執行程式碼時所耗費的記憶體容量
* 空間複雜度考慮的是記憶體的大小
* 以下為python簡單實例，可看記憶體使用狀況
```python
from memory_profiler import profile

@profile
def my_func():
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    c = [3] * (2 * 10 ** 8)
    del b
    return a    
  
if __name__=='__main__':
  my_func()
```
```
(env) yucheng@ubuntu:~/Algorithm-and-Data-Analysis/iThome_Algorithm$ python3 -m memory_profiler Space_Complexity.py
Filename: Space_Complexity.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     3     39.9 MiB     39.9 MiB           1   @profile
     4                                         def my_func():
     5     47.5 MiB      7.6 MiB           1       a = [1] * (10 ** 6)
     6    200.1 MiB    152.6 MiB           1       b = [2] * (2 * 10 ** 7)
     7   1726.1 MiB   1526.0 MiB           1       c = [3] * (2 * 10 ** 8)
     8   1573.5 MiB   -152.6 MiB           1       del b
     9   1573.5 MiB      0.0 MiB           1       return a    
```
