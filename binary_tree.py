

class Node:
    def __init__(self, value=None):
        self.value = value
        self.parent = None
        self.child_l = None
        self.child_r = None
        self.step = 0


def create_tree(values):

    def insert_node(node, value):

        if node.value == None:
            node.value = value

        elif value < node.value:
            if node.child_l == None:
                node.child_l = Node(value)
                node.child_l.parent = node
            else:
                 insert_node(node.child_l, value)

        elif value > node.value:
            if node.child_r == None:
                node.child_r = Node(value)
                node.child_r.parent = node
            else:
                insert_node(node.child_r, value)

    root = Node()
    for num in values:
        insert_node(root, num)

    return root



def search_node(node, value, total_steps):
    total_steps += 1

    if node.value > value:
        if node.child_l == None:
            return None
        else:
            return search_node(node.child_l, value, total_steps)

    elif node.value < value:
        if node.child_r == None:
            return None
        else:
            return search_node(node.child_r, value, total_steps)
    else:
        node.step = total_steps
        return node


values = [2,5,8,1,3,0,6,4,7]
root = create_tree(values)

costs = {}

for value in values:
    total_steps = -1
    node = search_node(root, value, total_steps)
    costs[node.value] = node.step





