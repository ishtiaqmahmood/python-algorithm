from collections import defaultdict


class NaiveBayes:
    """
    Naive Bayes Classifier for categorical features.
    """
    def __init__(self):
        self.class_probs = {}
        self.feature_probs = defaultdict(lambda: defaultdict(dict))

    def fit(self, X, y):
        n = len(y)
        for label in set(y):
            self.class_probs[label] = y.count(label) / n

        for label in self.class_probs:
            indices = [i for i, val in enumerate(y) if val == label]
            for j in range(len(X[0])):
                features = [X[i][j] for i in indices]
                for val in set(features):
                    self.feature_probs[label][j][val] = features.count(val) / len(indices)

    def predict(self, X):
        res = []
        for x in X:
            best_label, max_prob = None, -1
            for label in self.class_probs:
                prob = self.class_probs[label]
                for j, val in enumerate(x):
                    prob *= self.feature_probs[label][j].get(val, 0)
                if prob > max_prob:
                    max_prob, best_label = prob, label
            res.append(best_label)
        return res


if __name__ == "__main__":
    X = [['Sunny', 'Hot'], ['Sunny', 'Hot'], ['Overcast', 'Hot'], ['Rain', 'Mild']]
    y = ['No', 'No', 'Yes', 'Yes']
    nb = NaiveBayes()
    nb.fit(X, y)
    print(f"Predict ['Sunny', 'Mild']: {nb.predict([['Sunny', 'Mild']])}")
