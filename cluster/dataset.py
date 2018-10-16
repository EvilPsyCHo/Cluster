# coding:utf8
# @Time    : 18-10-16 下午4:36
# @Author  : evilpsycho
# @Mail    : evilpsycho42@gmail.com

import pandas as pd

from cluster.utils import get_dataset_path


def load_time_series(dim=1):
    assert dim in [1], "Only support dim={1}"
    p = get_dataset_path(f"time_series_{dim}d.csv")
    res = pd.read_csv(str(p))
    return res


if __name__ == "__main__":
    t_1d = load_time_series(1)
    print(t_1d.columns)