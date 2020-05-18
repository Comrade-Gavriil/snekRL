import numpy as np
from random import random, randint

def greedy(action_space):
    return np.argmax(action_space)

def epsilon_greedy(action_space, epsilon):
    e = epsilon
    temp = random()
    if e>=temp:
        return randint(0,len(action_space)-1)
    else:
        return greedy(action_space)


    