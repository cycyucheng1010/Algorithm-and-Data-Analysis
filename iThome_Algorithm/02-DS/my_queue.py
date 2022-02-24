import queue

# 先入先出
q = queue.Queue()
q.put(1)
print(q.get())
q.put(2)
print(q.get())
q.put(3)
print(q.get()) 

# 後入先出
q1 = queue.LifoQueue()
q1.put(2)
print(q1.get())
q1.put(4)
print(q1.get())
q1.put(6)
print(q1.get())

# 優先順序
q2 = queue.PriorityQueue()
q2.put("a")
print(q2.get())
q2.put("b")
print(q2.get())
q2.put("c")
print(q2.get()) #會先出前面的資料