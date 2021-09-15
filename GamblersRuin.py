import numpy as np
from numpy.linalg import matrix_power

from numpy import linalg  as la

from scipy import linalg  as scla

success_prob = 0.45
failure_prob = 1 - success_prob

p = np.array([  [1, 0,0,0,0,0,0,0,0,0,0 ], 
                [failure_prob, 0,success_prob,0,0,0,0,0,0,0 ,0], 
                [0, failure_prob, 0,success_prob,0,0,0,0,0,0,0], 
                [0, 0,failure_prob, 0,success_prob,0,0,0,0,0,0], 
                [0,0,0, failure_prob, 0,success_prob,0,0,0,0,0], 
                [0,0,0,0, failure_prob, 0,success_prob,0,0,0,0], 
                [0,0,0,0,0, failure_prob, 0,success_prob,0,0,0], 
                [0,0,0,0,0,0, failure_prob, 0,success_prob,0,0], 
                [0,0,0,0,0,0,0, failure_prob, 0,success_prob,0],
                [0,0,0,0,0,0,0, 0,failure_prob, 0,success_prob], 
                [0,0,0,0,0,0,0, 0, 0,0,1], 
                ]) 

initial_dist = np.array([[0,0,0,0,0,1,0,0,0,0,0]]) 

print(np.round(p,15))


n= 100
# for i in range(2) :
p2 = np.round(matrix_power(p, n), 3)   
# print (n, p2) 
p_n =np.matmul(initial_dist, p2)
print(n, p_n)