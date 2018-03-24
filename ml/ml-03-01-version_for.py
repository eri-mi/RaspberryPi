# -*- coding: utf-8 -*-
ExistsFlags = {}

try:
	import sklearn
	sklearnExists = True
	ExistsFlags[sklearn] = sklearnExists
except ImportError:
	sklearnExists = False

try:
	import numpy
	numpyExists = True
	ExistsFlags[numpy] = numpyExists
except ImportError:
	numpyExists = False

try:
	import scipy
	scipyExists = True
	ExistsFlags[scipy] = scipyExists
except ImportError:
	scipyExists = False

try:
	import matplotlib
	matplotlibExists = True
	ExistsFlags[matplotlib] = matplotlibExists
except ImportError:
	matplotlibExists = False

try:
	from PIL import Image
	PILExists = True
	ExistsFlags[Image] = PILExists
except ImportError:
	PILExists = False

try:
	import keras
	kerasExists = True
	ExistsFlags[keras] = kerasExists
except ImportError:
	kerasExists = False

try:
	import theano
	theanoExists = True
	ExistsFlags[theano] = theanoExists
except ImportError:
	theanoExists = False

# for分で纏めたい
for key, flag in ExistsFlags.items():
	if flag == True:
		if key != Image:
			print('{0}のバージョンは{1}です'.format(key.__name__, key.__version__))
		else:
			print('{0}のバージョンは{1}です'.format(key.__name__, key.PILLOW_VERSION))
	else:
		print('{0}はインストールされていません'.format(key))