# accidents probability insurance 

import numpy as np
from numpy.linalg import matrix_power

from numpy import linalg  as la

from scipy import linalg  as scla

p = np.array([  [.95, 0.05], 
                [0.98, 0.02]
                ]) 

initial_dist = np.array([[990,10]]) 

print(np.round(p,2))

p2 = np.round(matrix_power(p, 2), 10)    
p_n =np.matmul(initial_dist, p2)
print(p_n)