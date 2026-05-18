import math


class LogisticRegression:
    def __init__(self, lr=0.1, iterations=1000):
        self.lr = lr
        self.iterations = iterations

    def _sigmoid(self, z):
        return 1 / (1 + math.exp(-z))

    def fit(self, X, y):
        n_samples, n_features = len(X), len(X[0])
        self.weights = [0] * n_features
        self.bias = 0

        for _ in range(self.iterations):
            for i in range(n_samples):
                z = sum(X[i][j] * self.weights[j] for j in range(n_features)) + self.bias
                prediction = self._sigmoid(z)
                error = prediction - y[i]
                for j in range(n_features):
                    self.weights[j] -= self.lr * error * X[i][j]
                self.bias -= self.lr * error

    def predict(self, X):
        res = []
        for x in X:
            z = sum(x[j] * self.weights[j] for j in range(len(self.weights))) + self.bias
            res.append(1 if self._sigmoid(z) >= 0.5 else 0)
        return res


if __name__ == "__main__":
    X = [[1, 2], [2, 3], [3, 4], [6, 7], [7, 8], [8, 9]]
    y = [0, 0, 0, 1, 1, 1]
    model = LogisticRegression()
    model.fit(X, y)
    print(f"Predict [5, 5]: {model.predict([[5, 5]])}")
