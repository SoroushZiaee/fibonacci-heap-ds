class Node(object):
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.child = self.right = self.left = None
        self.parents = None
        self.degree = 0
        self.marked = False

    def add_node(self, node):
        if self.child is None:
            self.child = [node]
            self._set_parent(node)
            self.degree += 1

        else:
            self.child.append(node)
            self._set_parent(node)
            self.degree += 1

    def delete_node(self, node):
        self.child.remove(node)
        self.degree -= 1
        node.parent = None

    def _set_parent(self, node):
        if node.parents is None:
            node.parents = [self]
        else:
            node.parents.append(self)

    def get_value(self):
        return self.value

    def get_key(self):
        return self.key
