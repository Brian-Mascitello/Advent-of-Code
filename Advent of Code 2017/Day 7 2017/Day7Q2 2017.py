"""
Author:     Brian Mascitello
Date:       12/7/2017
Websites:   http://adventofcode.com/2017/day/7
Info:       --- Day 7: Recursive Circus ---
"""

from anytree import Node, RenderTree, ZigZagGroupIter


def build_tree(input_data, root):
    splitlines = input_data.splitlines().copy()
    queue = [root]
    while splitlines:
        for line in splitlines:
            split = line.split()
            parent = split[0]
            node_parent = None
            for item in queue:
                if parent in item.__str__():
                    node_parent = item
                    break
            if node_parent in queue:
                queue.remove(node_parent)
                children = list()
                if len(split) > 2:
                    children = split[3:]
                for child in children:
                    child = child.strip(',')
                    child_weight = get_weight(input_data, child)
                    node_child = Node(name=child, parent=node_parent, weight=child_weight, balance_weight=None)
                    queue.append(node_child)
                splitlines.remove(line)


def get_data(input_text):
    with open(input_text) as file:
        data_from_file = file.read()
    file.close()
    return data_from_file


def get_weight(input_data, node_name):
    for line in input_data.splitlines():
        if node_name in line:
            split = line.split()
            if node_name == split[0]:
                node_weight = split[1]
                node_weight = node_weight[1:-1]
                node_weight = int(node_weight)
                return node_weight


def find_root_node(input_data):
    parent_list = list()
    child_list = list()
    for line in input_data.splitlines():
        split = line.split()
        parent_list.append(split[0])

        children = list()
        if len(split) > 2:
            children = split[3:]
        for child in children:
            child_list.append(child.strip(','))

    root_name = set(parent_list) - set(child_list)
    root_name = ''.join(root_name)  # converts to str

    root_weight = get_weight(input_data, root_name)

    return Node(name=root_name, parent=None, weight=root_weight, balance_weight=0)


def insert_balanced_weights(node_levels):
    for level in node_levels:
        for node in level:
            if node.children:
                summation = 0
                for kid in node.children:
                    summation += kid.balance_weight
                node.balance_weight = summation + node.weight
            else:
                node.balance_weight = node.weight


def wrong_weight(node_levels):
    for level in node_levels:
        for node in level:
            if node.children:
                balance_dictionary = dict()
                for kid in node.children:
                    if kid.balance_weight in balance_dictionary.keys():
                        balance_dictionary[kid.balance_weight] += 1
                    else:
                        balance_dictionary[kid.balance_weight] = 1
                for kid in node.children:
                    if balance_dictionary[kid.balance_weight] == 1:
                        del balance_dictionary[kid.balance_weight]
                        print(kid.name + ' is the wrong weight!')
                        new_weight = (int(list(balance_dictionary.keys())[0]) - kid.balance_weight) + kid.weight
                        print(str(new_weight) + ' should be it\'s new weight!')
                        return


# data = get_data('Day7Q1 2017 Example.txt')  # Test with example.
data = get_data('Day7Q1 2017 Input.txt')

root_node = find_root_node(input_data=data)

build_tree(input_data=data, root=root_node)

levels = list(reversed([[node for node in children] for children in ZigZagGroupIter(root_node)]))

insert_balanced_weights(node_levels=levels)

print(RenderTree(root_node))

wrong_weight(node_levels=levels)
