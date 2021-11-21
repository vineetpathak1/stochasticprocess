import numpy as np
from statistics import mean 
from random import choices

number_runs = 1000
number_generations = 25





offsprings_list = [0,1,2]
offsprings_pmf = [0.2, 0.3, 0.5]


mean_offspring = sum( [x * y for (x, y) in zip(offsprings_list, offsprings_pmf)])
print (mean_offspring)

extinction_generation =  []
survived_with_population = []

for num_runs in range (number_runs) :
    print ("run #" ,num_runs )
    population_in_generation = [1]
    i =0
    # for i in range(number_generations):x 
    while (i < number_generations) and  ( population_in_generation[-1] > 0):
        last_generation_ppulation = population_in_generation[i]
        current_generation_population = population_in_generation[i]
        # print("current_generation",i )
        # print("current_generation_population", current_generation_population)
        if current_generation_population > 0 :    
            # print (current_generation_population)
            num_offsprings_for_current_generation = 0
            for j in range(current_generation_population) :
                num_offsprings = choices(offsprings_list, offsprings_pmf) 
                # print("offspring count", num_offsprings[0])
                # population_in_generation.append(num_offsprings[0])
                # print ("population_in_generation", population_in_generation)
                num_offsprings_for_current_generation = num_offsprings_for_current_generation + num_offsprings[0]
                # print("i", i , "j", j, "num_offsprings_for_current_generation", num_offsprings_for_current_generation)
            population_in_generation.append(num_offsprings_for_current_generation)
            # print("population_in_generation", population_in_generation)
        i = i + 1

    # print (population_in_generation)

    last_generation_count = len(population_in_generation)-1
    last_generation_population  = population_in_generation[-1]
    

    if ( last_generation_count < number_generations) :
        extinction_generation.append(last_generation_count)
    else :
        survived_with_population.append(last_generation_population)

print (extinction_generation)
print("survived runs population", survived_with_population)
print ("% of runs extincted", len(extinction_generation)/num_runs)


# lenght_offspring_prob_distribution = len(offspring_prob_distribution)
# cumulative_distribution = []
# mean_offspring = 0
# prob = 0



# for i in range(lenght_offspring_prob_distribution) :
#     prob = prob + offspring_prob_distribution[i]
#     mean_offspring = mean_offspring + i * offspring_prob_distribution[i]
#     cumulative_distribution.append(prob)


# print(mean_offspring)   
# print(cumulative_distribution)



# threshold_sum_value_to_exceed = 1

# uniform_lower = 0
# uniform_higher = 1

# list_results = []

# for i in range( number_runs) :
#     counter = 0
#     sum = 0

#     while (sum < threshold_sum_value_to_exceed) :
#         x = np.random.uniform(uniform_lower, uniform_higher)
#         counter = counter + 1
#         sum = sum + x

#     list_results.append(counter)
    
#     avg_counter = mean(list_results) 
#     print ("avergae of rv counter",avg_counter)
#     max_counter = max(list_results)
#     print (max_counter)

#     for i in range (max_counter+1) :
#         count = list_results.count(i)
#         print (i, count)

# print(list_results)
