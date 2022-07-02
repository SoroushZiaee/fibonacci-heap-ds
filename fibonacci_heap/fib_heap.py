from .Node import Node


class FiboHeap(object):
    def __init__(self):
        self.root_list = []
        self.last_node = None
        self.min_node = None
        self.total_node = 0

    def insert_node(self, node: Node):
        # node = Node(key, value)
        self.root_list.append(node)
        if self.min_node is None or self.min_node.key > node.key:
            self.min_node = node
        self.total_node += 1

        return node

    def find_min(self):
        return self.min_node

    # Merge
    def union(self, heap):
        H = FiboHeap()
        H.min_node = self.min_node

        # Concatenate the root list
        H.root_list = self.root_list.extend(heap.root_list)

        # Update the min
        if H.min_node.key > heap.min_node.key:
            H.min_node = heap.min_node

        H.total_node = self.total_node + heap.total_node

        return H

    def extract_min(self):
        # Delete the min_node
        max_degree = max([item.degree for item in self.root_list]) + 1
        min_temp = self.min_node
        if self.min_node is not None:
            self.root_list.extend(self.min_node.child)
            for item in self.min_node.child:
                item.parents = None
            self.root_list.remove(self.min_node)
            if len(self.root_list) == 0:
                self.min_node = None
            else:
                self.min_node = self.root_list[0]
                self._consolidate(max_degree)
            self.total_node -= 1

        return min_temp

    def _consolidate(self, max_degree):
        # print(f"{max_degree =}")
        array = [None] * max_degree
        # Creating a Loop till no nodes with same degree is remained
        while len(self.root_list) != 0:
            x = self.root_list[0]
            degree = x.degree
            # print(f"{x.key =} -- {degree=}")
            self.root_list.remove(x)
            while array[degree] is not None:
                y = array[degree]
                if x.key > y.key:
                    x, y = y, x

                x.add_node(y)
                array[degree] = None
                degree += 1

            array[degree] = x

        self.min_node = None
        for item in array:
            if item is not None:
                self.root_list.append(item)
                if self.min_node is None or item.key < self.min_node.key:
                    self.min_node = item

    def delete_node(self, x):
        if x.key == self.min_node.key:
            return self.extract_min_node()
        else:
            self._decrease_key(x, self.min_node.key - 1)
            return self.extract_min_node()

    def decrease_key(self, x, k):
        if x.key < k:
            return None
        x.key = k
        y = x.parents[0]

        if y is not None and x.key < y.key:
            self._cut(x, y)
            self._cascading_cut(y)

        if x.key < self.min_node.key:
            self.min_node = x

    def _cut(self, x, y):
        self.root_list.append(x)
        y.delete_node(x)

        if x.marked:
            x.marked = False

    def _cascading_cut(self, y):
        if y.parents is not None:
            if not y.marked:
                y.marked = True
            else:
                self._cut(y, y.parents[0])
                self._cascading_cut(y.parents[0])
