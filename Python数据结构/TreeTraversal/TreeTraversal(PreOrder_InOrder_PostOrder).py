#!python3

class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    # Insert Node following binary searching tree principle
    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    # Inorder traversal
    # Left -> current node -> Right
    def inOrderTraversal(self):
        res = []
        if self.left:
            res = self.left.inOrderTraversal()
        res.append(self.data)
        if self.right:
            res += self.right.inOrderTraversal()
        return res

    # PostOrder traversal
    # Left -> Right -> current node
    def postOrderTraversal(self):
        res = []
        if self.left:
            res = self.left.postOrderTraversal()
        if self.right:
            res += self.right.postOrderTraversal()
        res.append(self.data)
        return res

    # PreOrder traversal
    # current node -> Left -> Right
    def preOrderTraversal(self):
        res = []
        res.append(self.data)
        if self.left:
            res += self.left.preOrderTraversal()
        if self.right:
            res += self.right.preOrderTraversal()
        return res


# construct tree
root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
print(f"preOrder: {root.preOrderTraversal()}")
print(f"InOrder: {root.inOrderTraversal()}")
print(f"postOrder: {root.postOrderTraversal()}")

