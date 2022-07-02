from fibonacci_heap import Node, FiboHeap


def create_nodes():
    root1 = Node(3)
    for item in [18, 52, 38]:
        temp_node = Node(item)
        root1.add_node(temp_node)

        if item == 18:
            temp_node.add_node(Node(39))
        if item == 41:
            temp_node.add_node(Node(41))

    root2 = Node(17)
    root2.add_node(Node(30))

    root3 = Node(24)
    for item in [26, 46]:
        temp_node = Node(item)
        root3.add_node(temp_node)
        if item == 26:
            temp_node.add_node(Node(35))

    print(f"{root3.child =}")

    return root1, root2, root3


# Test Case for Node
root = Node(key=0, value=None)
node = Node(key=15, value=None)

root.add_node(node)
print(root.child[0].get_key())
print(node.parents[0].get_key())
print(root.degree)


# Test the Fibo Heap
print("-" * 20 + "Test The Fibo Heap" + "-" * 20)
f = FiboHeap()

root1, root2, root3 = create_nodes()
f.insert_node(Node(23))
f.insert_node(Node(7))
f.insert_node(Node(21))

f.insert_node(root1)
f.insert_node(root2)
f.insert_node(root3)


print(f"min f : {f.find_min().get_key()}")
min_first = f.extract_min()
print(f"min f : {f.find_min().get_key()}")

for item in f.root_list:
    print(f"{item.get_key() = }")

# get node 52
x = f.root_list[1].child[1].child[0]
print(f"{x.get_key() = }")

f.decrease_key(x, 4)
for item in f.root_list:
    print(f"{item.get_key() = }")
