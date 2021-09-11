# Peridod Markov Chain with period = 2
# Chexk the matrix power , it fluctuares for the odd and even multiplier 

import numpy as np
from numpy.linalg import matrix_power

from numpy import linalg  as la

from scipy import linalg  as scla

p_3 = np.array([[0, 1, 0], 
                [0.5, 0,0.5], 
                [0, 1,0] 
                ]) 

p101 = matrix_power(p_3, 101)

print (p101)

