class Tree:
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.cargo)


def print_tree(tree):
    if tree is None: return
    print(tree.cargo,
          print_tree(tree.left),
          print_tree(tree.right))


left = Tree(2)
right = Tree(3)

root = Tree(1, left, right)

print_tree(root)
