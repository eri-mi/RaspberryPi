# -*- coding: utf-8 -*-
from skleran import datasets
import numpy as np

iris = datasets.load_iris()

x = iris.data
y = iris.target

print(x)
print(y)