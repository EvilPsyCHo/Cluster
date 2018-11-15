# coding: utf-8
# Author: Zhirui Zhou
# Mail  : evilpsycho42@gmail.com
# Time  : 10/18/18
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from matplotlib import cm


def plot_cluster_sequence(cluster_labels, sequence_index, ax):
    label_interval = int(len(sequence_index) / 20)
    ax.imshow(pd.get_dummies(cluster_labels), aspect="auto", cmap='Greys')
    ax.set_yticks(range(0, len(sequence_index), label_interval))
    ax.set_yticklabels(sequence_index[np.array(range(0, len(sequence_index), label_interval))].tolist())
    ax.set_title("Sequence of Cluster labels")
    return ax


def plot_cluster_2d(X, cluster_labels, ax, **kwargs):
    dim = X.shape[1]
    x = X.copy()
    n = np.unique(cluster_labels).size
    assert dim >= 2
    if dim != 2:
        x = PCA(2).fit_transform(x)
    for c in np.unique(cluster_labels):
        ax.scatter(
            x[cluster_labels == c, 0],
            x[cluster_labels == c, 1],
            c=cm.brg(c/n),
            label=c,
            **kwargs,
        )
    ax.legend()
    return ax
