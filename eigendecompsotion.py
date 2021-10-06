import numpy as np
from numpy.linalg import matrix_power

from numpy import linalg  as la

from scipy import linalg  as scla

# p = np.array([  [0.7, 0.3], 
#                 [0.2, 0.8]
#                 ]) 


# u, V = la.eig(p)
# V_inv = la.inv(V)

# eig_value_matrix = np.array([[u[0], 0], 
#                             [0, u[1]]
#                             ]) 

# print( V)
# print (eig_value_matrix)
# print(V_inv)

# p2 = np.round(matrix_power(eig_value_matrix, 100), 100) 
# print(p2)

# matrxi_prod1 = np.matmul(V,p2)
# matrix_prod2 = np.matmul(matrxi_prod1,V_inv)

# print(matrxi_prod1)
# print(matrix_prod2)



# p = np.array([  [-1, 1], 
#                 [2, -2]
#                 ]) 

p = np.array([  [-1, 1/2, 1/2], 
                [1, -2, 1],
                [0, 3, -3]
                ]) 

scalar_t = 10
p = p * scalar_t

# print (p)

exp1 = scla.expm(p)
print (exp1)

# u, V = la.eig(p)
# V_inv = la.inv(V)

# print (u)
# print (V)
# print (V_inv)







