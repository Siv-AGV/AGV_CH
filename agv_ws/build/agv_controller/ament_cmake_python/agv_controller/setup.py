from setuptools import find_packages
from setuptools import setup

setup(
    name='agv_controller',
    version='0.0.0',
    packages=find_packages(
        include=('agv_controller', 'agv_controller.*')),
)
