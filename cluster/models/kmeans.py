# coding: utf-8
# Author: Zhirui Zhou
# Mail  : evilpsycho42@gmail.com
# Time  : 11/5/18
import numpy as np
from sklearn.metrics import euclidean_distances


def _init_centers(x, k, random_state, method='random'):
    if method == 'random':
        centers = x[random_state.choice(x.shape[0], k, replace=False)]
    else:
        raise NotImplementedError
    return centers


class KMeans:
    def __init__(self, k, init='random', max_iter=30, verbose=0, random_state=42):
        self.k = k
        self.random_state = np.random.RandomState(random_state) if isinstance(random_state, int) else random_state
        self._max_iter = max_iter
        self._verbose = verbose
        self._init = init
        self.score = np.inf
        self.centers = None
        self.labels = None

    def fit(self, x):
        centers = _init_centers(x, self.k, self.random_state, method=self._init)
        score_verbose = []
        for i in range(self._max_iter):
            distances_matrix = euclidean_distances(x, centers)
            labels = np.argmin(distances_matrix, axis=1)
            distances = np.min(distances_matrix, axis=1)
            self.score = np.sum(distances)
            score_verbose.append(self.score)
            for c in np.unique(labels):
                centers[c] = x[labels == c].mean(axis=0)
            if self._verbose > 0:
                if i % 5 == 0:
                    print(f'Iterations {i: 5} SSE {score_verbose[-1]: .2f}')
            if i > 10 and score_verbose[-1] - score_verbose[-2] < 1e-4:
                print(f'Convergence in Iterations {i:} , SSE {score_verbose[-1]: .2f}')
                break
        self.centers = centers
        self.labels = labels
        return self

    def predict(self, x):
        distances_matrix = euclidean_distances(x, self.centers)
        labels = np.argmin(distances_matrix, axis=1)
        return labels

    def fit_predict(self, x):
        self.fit(x)
        return self.predict(x)
