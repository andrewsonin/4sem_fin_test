class Tree:
    def __init__(self, val=None):
        self.left = self.right = None
        self.val = val

    def push(self, val):
        if self.val is None:
            self.val = val
        elif val < self.val:
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

    def remove(self, val, prev=None, prev_dir=None):
        if self.val is None:
            return
        if val > self.val:
            if self.right is not None:
                self.right.remove(val, self, 'r')
        elif val < self.val:
            if self.left is not None:
                self.left.remove(val, self, 'l')
        else:
            if self.left == None == self.right:
                if prev is None:
                    self.val = None
                elif prev_dir == 'l':
                    prev.left = None
                else:
                    prev.right = None
            elif self.left is None or self.right is None:
                if self.right is None:
                    child = self.left
                else:
                    child = self.right
                if prev is not None:
                    if prev_dir == 'l':
                        prev.left = child
                    else:
                        prev.right = child
                else:
                    self.val = child.val
                    self.right, self.left = child.right, child.left
            else:
                if self.right.left is None:
                    self.val = self.right.val
                    self.right = self.right.right
                else:
                    cur = self.right
                    previous = self.right
                    while cur.left is not None:
                        previous = cur
                        cur = cur.left
                    self.val = cur.val
                    previous.remove(self.val, previous, 'l')

my = Tree()
for i in [4, 435, 2, 35, 23, 454, 435345, 1, 834, 34, 34345]:
    my.push(i)
my.remove(435345)
my.print()
