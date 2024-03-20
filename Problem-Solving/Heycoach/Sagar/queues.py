""" doubly ended queue """
from collections import deque 


q = deque()

q.append(2)
q.append(3)
q.append(5)

print(q.pop()) #last element i.e removing from the last of the queue

print(q.popleft()) #removing from the left side of queue

print(q.appendleft(9)) #adding the element to the left side of the queue

sorted()