import math

from fibonacci_heap import FibonacciHeap


f = FibonacciHeap()

f.insert_node(10)
f.insert_node(2)
f.insert_node(15)
f.insert_node(6)

x = f.root_list.right
print(f"x : {x.key}")
f.delete_node(x)

x = f.root_list.right
print(f"new x : {x.key}")

m = f.find_min_node()
print(f"min : {m.key}")  # 2

q = f.extract_min_node()
print(f"extracted key :{q.key}")  # 2

q = f.extract_min_node()
print(f"extracted key :{q.key}")  # 6

print("Merge The two fibonacci heap...")
f2 = FibonacciHeap()
f2.insert_node(100)
f2.insert_node(56)

f3 = f.merge(f2)

# Delete a node by its key
