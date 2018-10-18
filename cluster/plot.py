# coding: utf-8
# Author: Zhirui Zhou
# Mail  : evilpsycho42@gmail.com
# Time  : 10/18/18
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from matplotlib import cm


def plot_cluster_sequence(cluster_labels, sample_index, ax):
    ax.imshow(pd.get_dummies(cluster_labels), aspect="auto", cmap='Greys')
    ax.set_yticks(range(0, len(sample_index), 20))
    ax.set_yticklabels(sample_index[np.array(range(0, len(sample_index), 20))].tolist())
    ax.set_title("Sequence of Cluster labels")


def plot_cluster_dim_reduction(X, cluster_labels, ax, dim_reduction=PCA(2)):
    dim = X.shape[1]
    x = X.copy()
    n = np.unique(cluster_labels).size
    assert dim >= 2
    if dim != 2:
        x = dim_reduction.fit_transform(x)
    for c in np.unique(cluster_labels):
        ax.scatter(x[cluster_labels == c, 0], x[cluster_labels == c, 1], c=cm.brg(c/n), label=c)
    ax.set_title("Dimension Reduction Plot")
    ax.legend()
