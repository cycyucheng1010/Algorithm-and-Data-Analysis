import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mglearn
from sklearn.datasets import load_iris
# data set
iris = load_iris()
print(iris.keys())
x = iris.data
y = iris.target
print(x.shape)
print(x[:5])
print('result:',y)
print('feature name',iris.feature_names)
print('target name:',iris.target_names)
print('\n',iris.DESCR)

# exercise
x, y = mglearn.datasets.make_forge()
print(x)
print(y)
mglearn.discrete_scatter(x[:,0],x[:,1],y)
plt.legend(['class0','class1'],loc=(1.02,0))
plt.xlabel('first feature')
plt.ylabel('second feature')
plt.show()

x,y  = mglearn.datasets.make_wave()
plt.plot(x,y,'o')
plt.ylim(-3,3)
plt.xlabel('feature')
plt.ylabel('target')
plt.show()
print(x)
print(y)