from collections import deque

# Declaring deque
queue = deque(['name', 'age', 'DOB']) #normal deque (better complexity)
ring_buffer = deque([], maxlen=10) #ring buffer!
print(queue)
