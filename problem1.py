from itertools import combinations

from fun import main
import random
import datetime
def generate_active_lists(num_elements, num_active):
    active_combinations = combinations(range(num_elements), num_active)
    activation_lists = []
    for active_indices in active_combinations:
        activation_list = [0]*num_elements
        for i in active_indices:
            activation_list[i] = 1
        activation_lists.append(activation_list)
    return activation_lists


active_lists = generate_active_lists(10, 5)  # Generate all possible active lists with 10 elements and 5 of them are active
for active_list in active_lists:
    print(active_list)
    main(active_list)