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

    heuristics = []
    positions = []

    for i, row in enumerate(values):
        for j, num in enumerate(row):
            insert_node(root, num)
            positions.append({num: [i, j]})

    for index, pos in enumerate(positions):
        print(index, pos.items())

    return root



def search_node(node, value, total_steps):
    total_steps += 1

    if node.value > value:
        if node.child_l == None:
            return None
        else:
            return search_node(node.child_l, step, total_steps)

    elif node.value < value:
        if node.child_r == None:
            return None
        else:
            return search_node(node.child_r, step, total_steps)
    else:
        node.step = total_steps
        return node


def set_heurisc(insert_node):
    pass



values = [ [2,5,8],
                   [1,3,0],
                   [6,4,7] ]



root = create_tree(values)

costs = set_heurisc(root)

""" for step in range(1, 10):
    total_steps = -1
    node = search_node(root, step, total_steps)
    costs[node.step] = node.value """


""" for i in costs:
    print(i) """


