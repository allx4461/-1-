import random
import numpy as np

def generate_fortest(size,r):
    arr1 = np.random.choice(np.arange(0, 10**5, 2), size=size)
    arr2 = np.random.choice(np.arange(1, 10**5, 2), size=size//r)
    arr1.sort()
    arr2.sort()
    return [arr1, arr2]
