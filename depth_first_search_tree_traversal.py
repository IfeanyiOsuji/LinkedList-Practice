class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def get_value(self):
        return self.value

    def set_left_child(self, left):
        self.left_child = left

    def set_right_child(self, right):
        self.right_child = right

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def has_left_child(self):
        return self.left_child is not None

    def has_right_child(self):
        return self.right_child is not None

    def __repr__(self):
        return f"Node({self.get_value()})"

    def __str__(self):
        return f"Node({self.get_value()})"


class Tree:
    def __init__(self, value= None):
        self.root = Node(value)

    def get_root(self):
        return self.root


def pre_order_traversal(tree):
    """
    In pre order traversal, we visit the root node, traverse through the left and then traverse through
    the right
    """
    visit_order = list()
    root = tree.get_root()

    def reverse(node):
        if node:
            visit_order.append(node.get_value()) # visit the node
            reverse(node.get_left_child()) # traverse the left child
            reverse(node.get_right_child()) # traverse the right child

    reverse(root)
    return visit_order

def in_order_traversal(tree):
    """
    in in order traversal, we traverse the left child, visit the node then traverse the right child
    """
    visit_order = list()
    root = tree.get_root()

    def reverse(node):
        if node:
            reverse(node.get_left_child()) # traverse the left child
            visit_order.append(node.get_value()) # visit the node
            reverse(node.get_right_child()) # traverse the right child

    reverse(root)
    return visit_order


def post_order_traversal(tree):
    """
    in post order traversal, we traverse the left child, traverse the right child, then
    visit the node
    """
    visit_order = list()
    root = tree.get_root()

    def reverse(node):
        if node:
            reverse(node.get_left_child())  # traverse the left child
            reverse(node.get_right_child())  # traverse the right child
            visit_order.append(node.get_value())  # visit the node

    reverse(root)
    return visit_order


tree = Tree("Apple")
tree.get_root().set_left_child(Node("Banana"))
tree.get_root().set_right_child(Node("Cherry"))
tree.get_root().get_left_child().set_left_child(Node("Dates"))

print(pre_order_traversal(tree))
print(in_order_traversal(tree))
print(post_order_traversal(tree))