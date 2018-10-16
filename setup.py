# coding:utf8
# @Time    : 18-10-16 下午6:06
# @Author  : evilpsycho
# @Mail    : evilpsycho42@gmail.com
from setuptools import setup


setup(
    name='cluster',
    version='0.1.0',
    description='cluster analysis framework',
    long_description='An interface-friendly and high-performance cluster analysis framework.',
    author=['Zhirui Zhou'],
    author_email=['evilpsycho42@gmail.com'],
    packages=['cluster'],
    package_data={'cluster': ['dataset_for_testing/*.csv']}
)
