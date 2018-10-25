# coding: utf-8
# Author: Zhirui Zhou
# Mail  : evilpsycho42@gmail.com
# Time  : 10/19/18
import numpy as np
import pandas as pd


def transition_probability_matrix(sequence):
    """聚类标签具有时间序列属性的标签转移概率矩阵计算

    Args:
        sequence: array like

    Returns:

    """
    size = len(sequence)
    states = list(set(sequence))
    states.sort()
    states2id = {s: idx for idx, s in enumerate(states)}
    id2states = {v: k for k, v in states2id.items()}
    m = np.zeros([len(states), len(states)])
    for i in range(size - 1):
        m[states2id[sequence[i]], states2id[sequence[i + 1]]] += 1
    m += 1
    m /= m.sum(axis=1).reshape(-1, 1)
    label_index = [i[0] for i in sorted(states2id.items(), key=lambda kv: kv[1], reverse=False)]
    m = pd.DataFrame(m, columns=label_index, index=label_index)
    return m
