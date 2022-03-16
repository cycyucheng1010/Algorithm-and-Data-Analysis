from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
cancer = load_breast_cancer()
x = cancer.data
y = cancer.target
x_train , x_test ,y_train ,y_test = train_test_split(x,y,stratify=y,random_state=0)
print(x_train)
print(y_train)