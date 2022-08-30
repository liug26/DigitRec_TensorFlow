import numpy as np
import pickle

pickle_path = "network.pickle"
txt_path = "network.txt"

'''
the pickle way of saving and reading network is convenient and fast in python, but it will be hard to transfer pickle 
files across different programming languages
'''


# reads and loads network at network_path
def save(model):
    with open(pickle_path, 'wb') as handle:
        pickle.dump(model, handle)
    print("network saved")


# saves the network at network_path
def load():
    with open(pickle_path, 'rb') as handle:
        model = pickle.load(handle)
    print("network loaded")
    return model