from components import ControllerNode, Node, os
from patterns import lets_hash, query_hash
import pandas as pd
import sys

BASEPATH = os.path.abspath("./")

if __name__ == "__main__":

    master = ControllerNode(ctrlnode_path=BASEPATH)
    if os.listdir("{}/node_pool".format(BASEPATH)): 
        master.get_nodes()
    else: 
        master.setup_nodes(3)

    if sys.argv[1] == "save":
        table = pd.read_csv("boston_house_prices.csv", header=[1])
        master.save_table("boston", table, lets_hash, hash_columns = "AGE")
    
    elif sys.argv[1] == "load":
        print(master.load_table("boston", query_hash))
    else: 
        pass 