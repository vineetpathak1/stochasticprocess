import numpy as np
from numpy.linalg import matrix_power

from numpy import linalg  as la

from scipy import linalg  as scla



p = np.array([[0.6, 0.4], [0.2, 0.8]]) 



# p2 = matrix_power(p, 2)

# print ( "tpm after 2 steps")
# print(p2)

# initial_dist = np.array([[1, 0]]) 

# tomorrow_weather =np.matmul(initial_dist, p)

# print ("tomrrow weather")
# print (tomorrow_weather)


# day_after_tomorrow_weather =np.matmul(initial_dist, p2)

# print ("day after tomrrow weather")
# print (day_after_tomorrow_weather)



p = np.array([  [0.7, 0, 0.3,0], 
                [0.5,0,  0.5, 0],
                [0, 0.4, 0, 0.6],
                [0, 0.6, 0, 0.4]
                ]) 

initial_dist = np.array([[0,0 ,0,1]]) 

p2 = matrix_power(p, 2)
# print(p2)

p3 = matrix_power(p, 3)

print ( "wednesday")
wednesday =np.matmul(initial_dist, p)
print (wednesday)



print ( "thursday")
thursday =np.matmul(initial_dist, p2)
print (thursday)

print ( "friday")
friday =np.matmul(initial_dist, p3)
print (friday)

p100 = matrix_power(p, 100)
print(p100)

# w,v = scla.eig(p, left=True,right=False)

# print (w)
# print (v)











p_3 = np.array([[0, 1, 0], 
                [0.5, 0,0.5], 
                [0, 1,0] 
                ]) 

p101 = matrix_power(p_3, 100)

print(p101)

# w,v = scla.eig(p_3, left=True,right=False) [0]

# print (w)
# print (v)
