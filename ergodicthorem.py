# accidents probability insurance 

import numpy as np
from numpy.linalg import matrix_power

from numpy import linalg  as la

from scipy import linalg  as scla

p = np.array([  [.7, 0.3], 
                [0.2, 0.8]
                ]) 

initial_dist = np.array([[0.4,0.6]]) 

print(np.round(p,15))



for i in range(2) :
    p2 = np.round(matrix_power(p, i), 10)   
    print (i, p2) 
    p_n =np.matmul(initial_dist, p2)
    print(i, p_n)