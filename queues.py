from queue import deque
queue = deque()
queue.append(10)
queue.append(20)
queue.append(30) 
print(queue) #print queue
queue.popleft() #pop top element
print(queue)
print(len(queue)) #length of queue
print(len(queue)==0) #is empty
