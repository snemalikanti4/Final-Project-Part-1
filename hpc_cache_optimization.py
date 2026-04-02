"""
High-Performance Computing (HPC) Optimization Project
Demonstration of Cache-Friendly Data Structure Optimization
"""

import numpy as np
import time

# -------------------------------
# Function: Naive Matrix Multiplication
# -------------------------------
def naive_matrix_multiplication(A, B):
    """
    Multiply matrices A and B using a naive triple-loop approach.
    
    Parameters:
        A (np.ndarray): Left matrix
        B (np.ndarray): Right matrix
        
    Returns:
        C (np.ndarray): Resulting matrix
    """
    N = A.shape[0]
    C = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            for k in range(N):
                C[i, j] += A[i, k] * B[k, j]
    return C

# -------------------------------
# Function: Optimized Matrix Multiplication
# -------------------------------
def optimized_matrix_multiplication(A, B):
    """
    Multiply matrices A and B using NumPy's optimized dot function.
    NumPy internally uses cache-friendly memory access and vectorized operations.
    
    Parameters:
        A (np.ndarray): Left matrix
        B (np.ndarray): Right matrix
        
    Returns:
        C (np.ndarray): Resulting matrix
    """
    return np.dot(A, B)

# -------------------------------
# Main Program
# -------------------------------
if __name__ == "__main__":
    # Matrix size
    N = 500  # Adjust based on your system memory

    # Generate random matrices
    A = np.random.rand(N, N)
    B = np.random.rand(N, N)

    # --- Naive Implementation ---
    start_naive = time.time()
    C_naive = naive_matrix_multiplication(A, B)
    end_naive = time.time()
    naive_time = end_naive - start_naive
    print(f"Naive Implementation Time: {naive_time:.4f} seconds")

    # --- Optimized Implementation ---
    start_opt = time.time()
    C_optimized = optimized_matrix_multiplication(A, B)
    end_opt = time.time()
    optimized_time = end_opt - start_opt
    print(f"Optimized Implementation Time: {optimized_time:.4f} seconds")

    # --- Performance Improvement ---
    improvement = ((naive_time - optimized_time) / naive_time) * 100
    print(f"Performance Improvement: {improvement:.2f}%")

    # Verify correctness
    if np.allclose(C_naive, C_optimized):
        print("Verification: Success! Both methods produce the same result.")
    else:
        print("Verification: Failed! Results differ.")
