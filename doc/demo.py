# coding:utf8
# @Time    : 18-9-1 上午10:53
# @Author  : evilpsycho
# @Mail    : evilpsycho42@gmail.com
from sklearn.cluster import AffinityPropagation
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import colors
import seaborn as sns
from sklearn.cluster import DBSCAN, KMeans, MiniBatchKMeans, Birch
from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler

def plot_cluster(x, index, cluster_id):
    unique_cid = np.unique(np.array(cluster_id))
    f, ax = plt.subplots(unique_cid.size, figsize=(12, 12))
    for idx, cid in enumerate(unique_cid):
        ax[idx].imshow(x[np.where(cluster_id==cid)])
        ax[idx].set_yticks(range((cluster_id==cid).sum()))
        ax[idx].set_yticklabels(index[np.where(cluster_id==cid)])
        ax[idx].set_title(f"cluster {idx}")

def plot_cluster_dim_reduction(x, cluster_id):
    x_dim_redc = PCA(n_components=2).fit_transform(data_scaler)
    f, ax = plt.subplots()
    ax.scatter(x_dim_redc[:, 0], x_dim_redc[:, 1], c=cluster_id, label=cluster_id)
    ax.legend()