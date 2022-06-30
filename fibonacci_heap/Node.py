class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.parent = self.child = self.right = self.left = None
        self.degree = 0
        self.marked = False

    def get_value(self):
        return self.value

    def get_key(self):
        return self.key
