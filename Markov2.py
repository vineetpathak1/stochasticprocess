# Dice thrown and state is maximum of the dice number till n throws ..

import numpy as np
from numpy.linalg import matrix_power

from numpy import linalg  as la

from scipy import linalg  as scla

p = np.array([  [0, 1/6, 1/6,1/6,1/6,1/6, 1/6], 
                [0, 1/6, 1/6,1/6,1/6,1/6, 1/6],
                [0, 0, 2/6,1/6,1/6,1/6, 1/6],
                [0, 0, 0,3/6,1/6,1/6, 1/6],
                [0, 0, 0,0,4/6,1/6, 1/6],
                [0, 0, 0,0,0,5/6, 1/6],
                [0, 0, 0,0,0,0, 1]
                ]) 

initial_dist = np.array([[1,0 ,0,0,0,0,0]]) 

print(np.round(p,2))

for i in range(10):

    p2 = np.round(matrix_power(p, i), 2)
    print("***************")
    print (i)
    print(p2)