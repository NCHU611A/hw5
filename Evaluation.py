# -*- coding: utf-8 -*-
"""
7110064039 徐人豪
Assignment #5: Matrix-Chain Multiplication

Evaluation:

1. Implement both algorithms in a programming language of your choice.
2. Test your implementations on a variety of input sizes and compare their running times.
3. Plot the running times of both algorithms on a graph with input size on the x-axis and running time on the y-axis.
4. Write a brief report that includes your observations and conclusions about the performance of the two algorithms.
"""

import matplotlib.pyplot as plt
import numpy as np
import random
import time

from Dynamic_Programming_Algorithm import matrix_chain_multiplication_dp
from Brute_Force_Algorithm import matrix_chain_multiplication_rec


running_times_dp = []
running_times_rec = []

n_number = 24

n_list = list(range(3,n_number+1,1))


for n in n_list:
    randomlist = random.sample(range(1, 100+1), n)
    
    start_dp = time.time()
    optimal_costs_dp, optimal_orders_dp = matrix_chain_multiplication_dp(randomlist)
    end_dp = time.time()
    running_times_dp.append(end_dp-start_dp)
    
    start_rec = time.time()
    optimal_cost_rec, optimal_order_rec = matrix_chain_multiplication_rec(randomlist)
    end_rec = time.time()
    running_times_rec.append(end_rec-start_rec)
    
    print('{}/{}\n'.format(n,n_number))


plt.plot(np.array(n_list), np.array(
        running_times_dp), label='dp')
plt.plot(np.array(n_list), np.array(
    running_times_rec), label='rec')


plt.xlabel("n")
plt.ylabel("running times")
plt.legend()
plt.show()