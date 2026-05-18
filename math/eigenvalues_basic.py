def power_iteration(A, num_simulations=100):
    """
    Power Iteration to find the dominant eigenvalue and eigenvector.
    """
    import random
    n = len(A)
    b_k = [random.random() for _ in range(n)]
    for _ in range(num_simulations):
        # Calculate matrix-vector product
        b_k1 = [sum(A[i][j] * b_k[j] for j in range(n)) for i in range(n)]
        # Normalize
        norm = sum(x**2 for x in b_k1)**0.5
        b_k = [x / norm for x in b_k1]

    # Rayleigh quotient for eigenvalue
    Ab = [sum(A[i][j] * b_k[j] for j in range(n)) for i in range(n)]
    eigenvalue = sum(b_k[i] * Ab[i] for i in range(n)) / sum(b_k[i]**2 for i in range(n))
    return eigenvalue, b_k


if __name__ == "__main__":
    A = [[0.5, 0.5], [0.2, 0.8]]
    val, vec = power_iteration(A)
    print(f"Dominant Eigenvalue: {val}")
