class LinearRegression:
    def __init__(self, lr=0.01, iterations=1000):
        self.lr = lr
        self.iterations = iterations
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        n_samples, n_features = len(X), len(X[0])
        self.weights = [0] * n_features
        self.bias = 0

        for _ in range(self.iterations):
            for i in range(n_samples):
                prediction = sum(X[i][j] * self.weights[j] for j in range(n_features)) + self.bias
                error = prediction - y[i]
                for j in range(n_features):
                    self.weights[j] -= self.lr * error * X[i][j]
                self.bias -= self.lr * error

    def predict(self, X):
        return [sum(x[j] * self.weights[j] for j in range(len(self.weights))) + self.bias for x in X]


if __name__ == "__main__":
    X = [[1], [2], [3]]
    y = [2, 4, 6]
    model = LinearRegression()
    model.fit(X, y)
    print(f"Prediction for [4]: {model.predict([[4]])}")
