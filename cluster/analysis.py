# coding: utf-8
# Author: Zhirui Zhou
# Mail  : evilpsycho42@gmail.com
# Time  : 10/19/18
import numpy as np


def transition_probability_matrix(sequence):
    size = len(sequence)
    states = {idx: s for idx, s in enumerate((set(sequence)).sort())}
    m = np.zeros([size, size])
    for i in range(size-1):
        m[states[sequence[i]], states[sequence[i+1]]] += 1
    m += 1
    m /= m.sum(axis=1)
    return m

