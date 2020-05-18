import numpy as np
from tensorflow import keras

class agent:
    
    def __init__(self, sub_agent, policy ):
        
        self.sub_agent = sub_agent
        self.policy = policy
        self.actions = {'n': [ 1,0], 'e': [0,1], 'w': []}
    
    def get_move (self, board):



class sub_agent:

    def __init__