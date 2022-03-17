# before coding 
## plz pip install sklearn pandas seaborn

# excercise1: Data_exploratory and visualization

import pandas as pd
import matplotlib.pyplot as plt
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier,plot_tree
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier, kneighbors_graph
from sklearn.svm import SVC
from sklearn.datasets import load_iris
data = pd.read_csv('/home/yucheng/Algorithm-and-Data-Analysis/HW/week5/Iris.csv')
print(data.head(5))
print(data.describe())
print(data.groupby('Species').size())

## holdout split
train,test = train_test_split(data,test_size=0.4,stratify=data['Species'],random_state=42)
n_bins =10
fig,axs = plt.subplots(2,2)
axs[0,0].hist(train['SepalLengthCm'],bins =n_bins)
axs[0,0].set_title('SepalLengthCm')
axs[0,1].hist(train['SepalWidthCm'],bins =n_bins)
axs[0,1].set_title('SepalWidthCm')
axs[1,0].hist(train['PetalLengthCm'],bins =n_bins)
axs[1,0].set_title('PetalLengthCm')
axs[1,1].hist(train['PetalWidthCm'],bins =n_bins)
axs[1,1].set_title('PetalWidthCm')

## add some spacing between subplots
fig.tight_layout(pad=1.0)
fig.show()

# excercise2: Decision tree
## split the x,y
x_train = train[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']]
y_train =train.Species
x_test = test[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']]
y_test = test.Species

## classification tree
mod_dt = DecisionTreeClassifier(max_depth=3,random_state=1)
mod_dt.fit(x_train,y_train)
Prediction = mod_dt.predict(x_test)
print('the accuracy of the decision tree is','{:.3f}'.format(metrics.accuracy_score(Prediction,y_test)))

fn = ['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']
cn = ['Iris-setosa','Iris-versicolor','Iris-virginica']
plt.figure(figsize=(10,8))
plot_tree(mod_dt,feature_names=fn,class_names=cn,filled=True)
plt.show()

#excercise3: KNN
mod_dt = KNeighborsClassifier()
mod_dt.fit(x_train,y_train)
prediction = mod_dt.predict(x_test)
print('the accuracy of the KNN is ','{:.3f}'.format(metrics.accuracy_score(prediction,y_test)))

# excercise4: SVC
mod_dt = SVC()
mod_dt.fit(x_train,y_train)
prediction = mod_dt.predict(x_test)
print('the accuracy of the SVC is ','{:.3f}'.format(metrics.accuracy_score(prediction,y_test)))

# excercise5: GaussianNB
mod_dt = GaussianNB()
mod_dt.fit(x_train,y_train)
prediction = mod_dt.predict(x_test)
print('the accuracy of the GaussianNB is ','{:.3f}'.format(metrics.accuracy_score(prediction,y_test)))