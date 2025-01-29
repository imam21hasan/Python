from collections import deque

info = deque(["Python", 5])
print(info)

info.append(10)
info.append(20)
print(info)

print("Top of queue : ", info[-1])

print("Popped item : ", info.popleft())
print(info)

print("Popped item : ", info.popleft())
print(info)
