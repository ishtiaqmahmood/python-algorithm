import random
import math


class KMeans:
    def __init__(self, k=3, max_iter=100):
        self.k = k
        self.max_iter = max_iter

    def _euclidean_distance(self, x1, x2):
        return math.sqrt(sum((a - b)**2 for a, b in zip(x1, x2)))

    def fit(self, X):
        self.centroids = random.sample(X, self.k)
        for _ in range(self.max_iter):
            clusters = [[] for _ in range(self.k)]
            for x in X:
                distances = [self._euclidean_distance(x, c) for c in self.centroids]
                cluster_idx = distances.index(min(distances))
                clusters[cluster_idx].append(x)

            new_centroids = []
            for cluster in clusters:
                if not cluster:
                    new_centroids.append(random.choice(X))
                else:
                    new_centroids.append([sum(dim)/len(cluster) for dim in zip(*cluster)])

            if new_centroids == self.centroids:
                break
            self.centroids = new_centroids

    def predict(self, X):
        res = []
        for x in X:
            distances = [self._euclidean_distance(x, c) for c in self.centroids]
            res.append(distances.index(min(distances)))
        return res


if __name__ == "__main__":
    X = [[1, 2], [1, 4], [1, 0], [10, 2], [10, 4], [10, 0]]
    km = KMeans(k=2)
    km.fit(X)
    print(f"Centroids: {km.centroids}")
