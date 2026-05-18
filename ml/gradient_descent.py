def gradient_descent(f, df, start_x, lr=0.1, iterations=100):
    """
    Basic Gradient Descent.
    """
    x = start_x
    for _ in range(iterations):
        x = x - lr * df(x)
    return x


if __name__ == "__main__":
    # f(x) = x^2, df(x) = 2x
    res = gradient_descent(lambda x: x**2, lambda x: 2*x, 10)
    print(f"Minima of x^2 starts from 10: {res}")
