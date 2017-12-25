from sklearn.metrics import classification_report, confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer


knn = KNeighborsClassifier(n_neighbors=8)
b_cancer = load_breast_cancer()
x_train, x_test, y_train, y_test = train_test_split(b_cancer.data, b_cancer.target,
                                                    test_size=0.2, random_state=1)

#print(x_train)
knn.fit(x_train, y_train)
y_pred = knn.predict(x_test)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
