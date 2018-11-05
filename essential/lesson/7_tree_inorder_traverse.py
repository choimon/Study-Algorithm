class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def init_tree():
    global root

    new_node = Node('A')
    root = new_node

    new_node = Node('B')
    root.left = new_node

    new_node = Node('C')
    root.right = new_node

    new_node_1 = Node('D')
    new_node_2 = Node('E')
    node = root.left
    node.left = new_node_1
    node.right = new_node_2

    new_node_1 = Node('F')
    new_node_2 = Node('G')
    node = root.right
    node.left = new_node_1
    node.right = new_node_2


# def inorder_traverse(node):
#
#     if node.left:
#         inorder_traverse(node.left)
#
#     print(node.data, end='-> ') if node.data != 'G' else print(node.data)
#
#     if node.right:
#         inorder_traverse(node.right)


def inorder_traverse(node):

    if node is None:
        return

    inorder_traverse(node.left)
    print(node.data, end='-> ') if node.data != 'G' else print(node.data)
    inorder_traverse(node.right)


if __name__ == '__main__':

    init_tree()
    node = root

    inorder_traverse(node)
