# weather prediction for next few days

import numpy as np
from numpy.linalg import matrix_power
from numpy import linalg  as la
from scipy import linalg  as scla


p = np.array([[0.6, 0.4], [0.2, 0.8]]) 

p2 = matrix_power(p, 2)

print ( "tpm after 2 steps")
print(p2)

initial_dist = np.array([[1, 0]]) 

tomorrow_weather =np.matmul(initial_dist, p)

print ("tomrrow weather")
print (tomorrow_weather)


day_after_tomorrow_weather =np.matmul(initial_dist, p2)

print ("day after tomrrow weather")
print (day_after_tomorrow_weather)


# weather prediciton if tomorrows waether is dependnet on last 2 days 

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


