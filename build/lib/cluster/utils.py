# coding:utf8
# @Time    : 18-10-16 下午4:38
# @Author  : evilpsycho
# @Mail    : evilpsycho42@gmail.com
import pathlib


def get_package_root_path():
    p = pathlib.Path(__file__).resolve().parent
    return p


def get_dataset_path(dataset_name):
    root = get_package_root_path()
    return root / "dataset_for_testing" / dataset_name


if __name__ == "__main__":
    print(get_package_root_path())
    print(get_dataset_path("time_series_1d.csv"))