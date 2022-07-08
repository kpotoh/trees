import json
import random
import sys

from ete3 import PhyloTree


def _rangen(a=50000, b=5000000):
    stor = set()
    while True:
        n = random.randint(a, b)
        if n in stor:
            continue
        yield n


rangen = _rangen()


def get_json(node):
    # Read ETE tag for duplication or speciation events
    if not hasattr(node, 'evoltype'):
        dup = random.sample(['N','Y'], 1)[0]
    elif node.evoltype == "S":
        dup = "N"
    elif node.evoltype == "D":
        dup = "Y"

    node.name = node.name.replace("'", '')
    idx = next(rangen)
    nleaves = len(node)
    nleaves = nleaves if nleaves > 1 else 0
        
    json = { 
        "name": node.name, 
        "numLeafs": nleaves,
        "ottId": f"ott{idx}",
        "branch_length": str(node.dist),
        }
    if node.children:
        json["children"] = []
        for ch in node.children:
            json["children"].append(get_json(ch))
    return json


def dump(data, path=None):
    kwargs = {
        "indent": 4,
    }
    if path is None:
        print(json.dumps(data, **kwargs))
    else:
        with open(path, 'w') as handle:
            json.dump(data, handle, **kwargs)
        

if __name__ == '__main__':
    if len(sys.argv) > 1:
        t = PhyloTree(sys.argv[1], format=1)
    else:
        # create a random example tree
        t = PhyloTree()
        t.populate(100, random_branches=True)
                   
    # TreeWidget seems to fail with simple quotes
    data = get_json(t)
    dump(data)
