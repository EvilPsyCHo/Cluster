# coding:utf8
# @Time    : 18-10-17 上午10:57
# @Author  : evilpsycho
# @Mail    : evilpsycho42@gmail.com
from sklearn.metrics import (
    adjusted_rand_score, homogeneity_score, completeness_score, adjusted_mutual_info_score,
    v_measure_score, fowlkes_mallows_score, silhouette_score, calinski_harabaz_score,
)
import numpy as np
import warnings
warnings.filterwarnings('ignore')


__all__ = [
    'adjusted_rand_score',  # 调整兰德系数
    'adjusted_rand_score_matrix',  # 调整兰德系数矩阵
    'adjusted_mutual_info_score',
    'adjusted_mutual_info_score_matrix',  #
    'homogeneity_score',
    'completeness_score',
    'v_measure_score',
    'fowlkes_mallows_score',
    'silhouette_score',
    'calinski_harabaz_score'
]


def adjusted_rand_score_matrix(*args):
    return _score_matrix(*args, evaluate_function=adjusted_rand_score)


def adjusted_mutual_info_score_matrix(*args):
    return _score_matrix(*args, evaluate_function=adjusted_mutual_info_score)


def _score_matrix(*args, evaluate_function):
    """
    Args:
        *args: list<list<string>>, shape=(n_cluster, n_sample), string denote the cluster_label
        evaluate_function: callable function
    Returns:
        score_matrix: ndarray
    """
    size = len(args[0])
    assert size >= 2, 'clusters must more than 2'
    score_matrix = np.zeros([size, size])
    for i in range(size):
        for j in range(size):
            if i == j:
                score_matrix[i, j] = 1.
            else:
                score_matrix[i, j] = evaluate_function(args[0][i], args[0][j])
    return score_matrix
