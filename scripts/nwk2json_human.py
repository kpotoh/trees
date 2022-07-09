import json
import random
import re
import sys

from ete3 import PhyloTree


def _rangen(a=50000, b=5000000):
    """ottId generation"""
    stor = set()
    max_size = b - a
    while True:
        n = random.randint(a, b)
        if n in stor:
            if len(stor) >= max_size:
                raise RuntimeError("Too big tree, cannot add ottId")
            continue
        yield n


ottId_rangen = _rangen()


def get_json(node):
    name = node.name.replace("'", "")
    if name.count("/") == 2:
        support1, support2, support3 = name.split("/")
        name = ""
    else:
        support1 = support2 = support3 = ""
    idx = next(ottId_rangen)
    nleaves = len(node)
    nleaves = nleaves if nleaves > 1 else 0
    json = {
        "ottId": f"ott{idx}",
        "name": name,
        # "display_label": name,
        # "common_name": name,
        # "type": "node" if node.children else "leaf",
        "numLeafs": nleaves,
        "branch_length": str(node.dist),
        # "support1": support1,
        # "support2": support2,
        # "support3": support3,
    }
    if node.children:
        json["children"] = []
        for ch in node.children:
            json["children"].append(get_json(ch))
    return json


def dump(data, path=None):
    kwargs = {"indent": 4}
    if path is None:
        print(json.dumps(data, **kwargs))
    else:
        with open(path, 'w') as handle:
            json.dump(data, handle, **kwargs)


if __name__ == '__main__':
    # if len(sys.argv) > 1:
        # t = PhyloTree(sys.argv[1], format=1)
        t = PhyloTree("data/human/GTR.reduced.treWsupports", format=1)
        data = get_json(t)
        dump(data)
    # else:
    #     raise RuntimeError("pass arguments: tree (nwk")

