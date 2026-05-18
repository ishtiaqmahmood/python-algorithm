import math
from collections import Counter


class KNN:
    def __init__(self, k=3):
        self.k = k

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def _euclidean_distance(self, x1, x2):
        return math.sqrt(sum((a - b)**2 for a, b in zip(x1, x2)))

    def predict(self, X):
        predictions = [self._predict(x) for x in X]
        return predictions

    def _predict(self, x):
        distances = [self._euclidean_distance(x, x_train) for x_train in self.X_train]
        k_indices = sorted(range(len(distances)), key=lambda i: distances[i])[:self.k]
        k_nearest_labels = [self.y_train[i] for i in k_indices]
        most_common = Counter(k_nearest_labels).most_common(1)
        return most_common[0][0]


if __name__ == "__main__":
    X = [[1, 2], [2, 3], [3, 1], [6, 5], [7, 7], [8, 6]]
    y = [0, 0, 0, 1, 1, 1]
    knn = KNN(k=3)
    knn.fit(X, y)
    print(f"Predict [5, 5]: {knn.predict([[5, 5]])}")
