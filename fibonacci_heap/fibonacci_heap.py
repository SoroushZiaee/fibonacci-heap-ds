import math
from Node import Node


class FibonacciHeap(object):
    def __init__(
        self,
    ):
        self.min_node = None
        self.root_list = None
        self.total_node = 0

    def find_min_node(self):
        return self.min_node

    def insert_node(self, key, value=None):
        node = Node(key, value)
        # Write this code just for Solving the bugs
        node.left = node.right = node
        self.merge_with_root_list(node)
        if self.min_node is None or self.min_node.key > node.key:
            self.min_node = node
        self.total_node += 1
        return node

    # Get the min_node of this tree and then remove it, then set another min for the tree
    def extract_min_node(self):
        min_temp = self.find_min_node()
        if min_temp is not None:
            if min_temp.child is not None:
                childs = [x for x in self._iterate(min_temp.child)]
                for i in range(0, len(childs)):
                    self.merge_with_root_list(childs[i])
                    childs[i].parent = None

            self.remove_from_root_list(min_temp)

            if min_temp == min_temp.right:
                self.min_node = self.root_list = None
            else:
                self.min_node = min_temp.right
                self._re_adjust()
            self.total_node -= 1
        return min_temp

    def merge(self, h2):
        H = FibonacciHeap()
        H.root_list, H.min_node = self.root_list, self.min_node
        # fix pointers when merging the two heaps
        last = h2.root_list.left
        h2.root_list.left = H.root_list.left
        H.root_list.left.right = h2.root_list
        H.root_list.left = last
        H.root_list.left.right = H.root_list
        # update min node if needed
        if h2.min_node.key < H.min_node.key:
            H.min_node = h2.min_node
        # update total nodes
        H.total_node = self.total_node + h2.total_node
        return H

    def delete_node(self, x):
        if x.key == self.min_node.key:
            return self.extract_min_node()
        else:
            self._decrease_key(x, self.min_node.key)
            return self.extract_min_node()

    def _decrease_key(self, x, k):
        if k > x.key:
            return None
        x.key = k
        y = x.parent
        if y is not None and x.key < y.key:
            self._cut(x, y)
            self._cascading_cut(y)
        if x.key < self.min_node.key:
            self.min_node = x

    # if a child node becomes smaller than its parent node we
    # _cut this child node off and bring it up to the root list
    def _cut(self, x, y):
        self.remove_from_child_list(y, x)
        y.degree -= 1
        self.merge_with_root_list(x)
        x.parent = None
        x.mark = False

    # cascading cut of parent node to obtain good time bounds
    def _cascading_cut(self, y):
        z = y.parent
        if z is not None:
            if y.mark is False:
                y.mark = True
            else:
                self._cut(y, z)
                self._cascading_cut(z)

    def _re_adjust(self):
        A = [None] * int(math.log(self.total_node) * 2)
        nodes = [w for w in self._iterate(self.root_list)]
        for w in range(0, len(nodes)):
            x = nodes[w]
            d = x.degree
            while A[d] != None:
                y = A[d]
                if x.key > y.key:
                    temp = x
                    x, y = y, temp
                self._heap_link(y, x)
                A[d] = None
                d += 1
            A[d] = x
        # find new min node - no need to reconstruct new root list below
        # because root list was iteratively changing as we were moving
        # nodes around in the above loop
        for i in range(0, len(A)):
            if A[i] is not None:
                if A[i].key < self.min_node.key:
                    self.min_node = A[i]

    # Update the link-list among the root list and update the childs' linklist
    def _heap_link(self, y, x):
        self.remove_from_root_list(y)
        y.left = y.right = y
        self.merge_with_child_list(x, y)
        x.degree += 1
        y.parent = x
        y.mark = False

    def merge_with_root_list(self, node: Node):

        if self.root_list is None:
            self.root_list = node
        else:
            node.right = self.root_list.right
            node.left = self.root_list
            self.root_list.right.left = node
            self.root_list.right = node

    # merge a node with the doubly linked child list of a root node
    def merge_with_child_list(self, parent, node):
        if parent.child is None:
            parent.child = node
        else:
            node.right = parent.child.right
            node.left = parent.child
            parent.child.right.left = node
            parent.child.right = node

    def _iterate(self, head):
        stop = node = head
        flag = False
        while True:
            if node == stop and flag is True:
                break
            elif node == stop:
                flag = True
            yield node
            node = node.right

    def remove_from_root_list(self, node):
        if node == self.root_list:
            self.root_list = node.right
        node.left.right = node.right
        node.right.left = node.left

    def remove_from_child_list(self, parent, node):
        if parent.child == parent.child.right:
            parent.child = None
        elif parent.child == node:
            parent.child = node.right
            node.right.parent = parent
        node.left.right = node.right
        node.right.left = node.left
