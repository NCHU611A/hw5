# -*- coding: utf-8 -*-
"""
7110064039 徐人豪
Assignment #5: Matrix-Chain Multiplication

matrix-chain multiplication problem

Algorithm 1: Brute-Force Algorithm
1. Write a recursive function to enumerate all possible parenthesizations of the matrix chain.
2. For each parenthesization, compute the number of scalar multiplications required to compute the product of the entire chain of matrices.
3. Return the minimum number of scalar multiplications found and the corresponding optimal parenthesization.
"""

import sys

def matrix_chain_order(p, i, j, brackets):
    if i == j:
        return 0
    
    min_cost = sys.maxsize
    optimal_brackets = None
    
    for k in range(i, j):
        cost = matrix_chain_order(p, i, k, brackets) + matrix_chain_order(p, k+1, j, brackets) + p[i-1] * p[k] * p[j]
        if cost < min_cost:
            min_cost = cost
            optimal_brackets = (k, brackets[i-1][k-1], brackets[k][j-1])
    
    brackets[i-1][j-1] = optimal_brackets
    return min_cost

def construct_optimal_parenthesization(brackets, i, j):
    if i == j:
        return "A" + str(i)
    else:
        k, left, right = brackets[i-1][j-1]
        return "(" + construct_optimal_parenthesization(brackets, i, k) + " x " + construct_optimal_parenthesization(brackets, k+1, j) + ")"

def matrix_chain_multiplication_rec(p):
    n = len(p) - 1
    brackets = [[None] * n for _ in range(n)]
    optimal_cost = matrix_chain_order(p, 1, n, brackets)
    optimal_order = construct_optimal_parenthesization(brackets, 1, n)
    return optimal_cost, optimal_order

if __name__=='__main__':
    # Example usage:
    dimensions = [10, 20, 30, 40, 30]  #(((AB)C)D)
    #dimensions = [40, 20, 30, 10, 30]  #((A(BC))D)
    
    optimal_cost, optimal_order = matrix_chain_multiplication_rec(dimensions)
    print("Optimal number of scalar multiplications:", optimal_cost)
    print("Optimal ordering of matrix multiplications:", optimal_order)