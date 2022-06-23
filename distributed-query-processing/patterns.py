import pandas as pd
import pickle
import os

def key_assign(key, nodes):
    chosen_node = None
    best = float("inf")
    for node in nodes:
        a = int(str(abs(key))[:3])
        b = int(str(abs(node.id_))[:3])
        dist = abs(a - b)
        if dist < best:
            best = dist
            chosen_node = node
    return {
            "node": chosen_node, 
            "key": key
        }

def lookup(key, nodes):
    for node in nodes:
        if node.is_key_owner(key):
            return node.get_data(key)


def lets_hash(name, table:pd.DataFrame, nodes, hash_column):
    keys = {}
    for i,ele in enumerate(table[hash_column]):
        row = table.iloc[i].to_dict()
        key = hash(str(ele))
        node_assignment = key_assign(key, nodes)
        chosen = node_assignment["node"]
        chosen.store(key, row)
        
        if not keys.__contains__(chosen.id_):
            keys[key] = []
        
        keys[key].append(chosen.id_)

    os.mkdir(name)
    with open("{}/hash_cache".format(name), "wb") as f:
        pickle.dump(keys ,f)


def query_hash(name, nodes):
    with open("{}/hash_cache".format(name), "rb") as f:
        keys = pickle.load(f)

    table = None
    i = 0
    for key, node_id in keys.items():
        i += 1
        
        data = dict([(k,[v]) for k,v in lookup(key, nodes).items()])

        if i == 1:
            table = pd.DataFrame(data)
            continue

        table = pd.concat([table, pd.DataFrame(data)])
    
    return table
            
    
