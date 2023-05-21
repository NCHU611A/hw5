# -*- coding: utf-8 -*-
"""
7110064039 徐人豪
Assignment #5: Matrix-Chain Multiplication

matrix-chain multiplication problem

Algorithm 2: Dynamic Programming Algorithm
1. Create a two-dimensional array m of size n x n, where m[i][j] will store the minimum number of scalar multiplications required to compute the product of matrices Ai through Aj.
2. Create a two-dimensional array s of size n x n, where s[i][j] will store the index k that achieves the minimum number of scalar multiplications for the subproblem of computing Ai through Aj.
3. Initialize the diagonal elements of m to 0.
4. For each chain length l from 2 to n, do the following:
      For each starting index i from 1 to n-l+1, do the following:
        Compute the ending index j = i + l - 1.
        Initialize m[i][j] to infinity.
        For each index k from i to j-1, do the following:
            Compute a temporary cost tempCost = m[i][k] + m[k+1][j] + P[i-1] * P[k] * P[j].
            If tempCost is less than m[i][j], update m[i][j] to tempCost and s[i][j] to k.
5. Return the minimum number of scalar multiplications found in m[1][n] and use s to construct the optimal parenthesization.
"""

import sys

def matrix_chain_multiplication_dp(p):
    n = len(p) - 1
    m = [[0] * n for _ in range(n)]
    s = [[0] * n for _ in range(n)]
    
    for l in range(2, n+1):
        for i in range(1, n-l+2):
            j = i + l - 1
            m[i-1][j-1] = sys.maxsize
            
            for k in range(i, j):
                cost = m[i-1][k-1] + m[k][j-1] + p[i-1] * p[k] * p[j]
                
                if cost < m[i-1][j-1]:
                    m[i-1][j-1] = cost
                    s[i-1][j-1] = k
    
    return m[0][n-1], construct_optimal_parenthesization(s, 1, n)

def construct_optimal_parenthesization(s, i, j):
    if i == j:
        return "A" + str(i)
    else:
        k = s[i-1][j-1]
        return "(" + construct_optimal_parenthesization(s, i, k) + " x " + construct_optimal_parenthesization(s, k+1, j) + ")"

if __name__=='__main__':
    # Example usage:
    dimensions = [10, 20, 30, 40, 30]  #(((AB)C)D)
    #dimensions = [40, 20, 30, 10, 30]  #((A(BC))D)
    
    optimal_cost, optimal_order = matrix_chain_multiplication_dp(dimensions)
    print("Optimal number of scalar multiplications:", optimal_cost)
    print("Optimal ordering of matrix multiplications:", optimal_order)