class Tree:
    def __init__(self, val=None):
        self.left = self.right = None
        self.val = val

    def push(self, val):
        if self.val is None:
            self.val = val
            return
        if val < self.val:
            if self.left is None:
                self.left = Tree(val)
            else:
                self.left.push(val)
        else:
            if self.right is None:
                self.right = Tree(val)
            else:
                self.right.push(val)

    def print(self):
        if self.left is not None:
            self.left.print()
        print(self.val)
        if self.right is not None:
            self.right.print()

    def find(self, key):
        if self.val is None:
            return False
        if self.val == key:
            return True
        if key < self.val:
            if self.left is not None:
                return self.left.find(key)
        else:
            if self.right is not None:
                return self.right.find(key)
        return False

my_tree = Tree()
for i in range(int(input())):
    my_tree.push(int(input()))
my_tree.print()
print(my_tree.find(int(input())))
