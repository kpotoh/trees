import json
from queue import Queue

import ete3
from ete3 import PhyloTree


def node_parent(node):
    try:
        return next(node.iter_ancestors())
    except BaseException:
        return None


def iter_tree_edges(tree: PhyloTree):
    discovered_nodes = set()
    discovered_nodes.add(tree.name)
    Q = Queue()
    Q.put(tree)

    while not Q.empty():
        cur_node = Q.get()
        for child in cur_node.children:
            Q.put(child)

        if cur_node.name not in discovered_nodes:
            discovered_nodes.add(cur_node.name)
            alt_node = cur_node
            ref_node = node_parent(alt_node)
            yield ref_node, alt_node


def to_json(t: PhyloTree):
    t.describe()
    print(f"len(t) = {len(t)}")
    print(t.get_ascii())


    for node1, node2 in iter_tree_edges(t):
        print(node1.name, node2.name)


    return


def dump(data, path):
    with open(path, 'w') as handle:
        json.dump(data, handle)


def main():
    path_to_tree = "./data/random_d3.tre"
    tree = PhyloTree(path_to_tree, format=1)
    data = to_json(tree)
    
    
    # dump(data)


if __name__ == "__main__":
    # main()

    import re

    with open("./data/mammalia.d3.json") as fin:
        ids = re.findall("\"ottId\": \"(.+)\"", fin.read())
        for x in ids:
            print(x)
