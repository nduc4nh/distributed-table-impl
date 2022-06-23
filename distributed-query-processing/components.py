from uuid import uuid4
import os, sys
import pickle


class Node:
    def __init__(self):
        self.id_ = None
        self.path = None
        self.map = {}
        
    @classmethod
    def get_instane(self, instance_path):
        with open(instance_path, "rb") as f:
            ins = pickle.load(f)
        return ins

    def persist(self):
        with open("{}/node_{}".format(self.path, self.id_), "wb") as f:
            pickle.dump(self, f)
    
    def make_instance(self, base_path):
        self.id_ = hash(uuid4().__str__())
        self.path = "{}/node_{}".format(base_path, self.id_)
        os.mkdir(self.path)
        self.persist()
        return self

    def store(self, key, data):
        data_path = "{}/data_{}".format(self.path, key)
        with open(data_path, "wb") as f:
            pickle.dump(data, f)
        self.map[key] = data_path
        self.persist()

    def is_key_owner(self, key):
        return key in self.map
    
    def get_data(self, key):
        with open(self.map[key], "rb") as f:
            data = pickle.load(f)
        return data

class ControllerNode:
    def __init__(self, ctrlnode_path) -> None:
        self.path = ctrlnode_path
        self.nodes = []

    def get_nodes(self):
        node_path = "{}/node_pool".format(self.path)
        node_names = [ele for ele in os.listdir(node_path) if "node_" in ele]
        for node_name in node_names:
            instance_path = os.path.join(node_path, node_name, node_name)
            self.nodes.append(Node.get_instane(instance_path))
        return self

    def setup_nodes(self, node_num):
        self.nodes = [Node().make_instance("{}/node_pool".format(self.path)) for i in range(node_num)]

    
    def save_table(self, name, table, alg, **kwargs):
        if kwargs.__contains__("hash_columns"):
            alg(name, table, self.nodes, kwargs["hash_columns"])
            return
        alg(table, self.nodes)

    def load_table(self,name, alg, **kwargs):
        return alg(name, self.nodes)      



        