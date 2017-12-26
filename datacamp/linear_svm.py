import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

data_source = load_iris()
X_train, X_test, Y_train, Y_test = train_test_split(data_source.data, data_source.target, test_size=50)


# ToDo add regularization
MARGIN = 1
M, FEATURES = X_train.shape
N_CLASS = 3
ALPHA = 0.001
ITERATIONS = 600
# weights
W = np.zeros((N_CLASS, FEATURES + 1))
ones = np.array([[1] * M])
_X = np.concatenate((ones.T, X_train), axis=1)

for k in range(ITERATIONS):
    for i in range(M):
        ans = Y_train[i]
        L = 0
        LL = 0
        for j in range(N_CLASS):
            if j != ans:
                Lj = max((W[j] - W[ans]).dot(_X[i]) + MARGIN, 0)
                L += Lj
                LL += Lj ** 2
                W[j, 1:] -= ALPHA * Lj * X_train[i]
        W[ans, 1:] += ALPHA / M * L * _X[i, 1:]
        print("loss:", LL)
    # it is not necessary to set b in this case, as the difference between predictions are relative)

    correct = 0
for i in range(X_test.shape[0]):
    correct += (np.argmax(W.dot(np.concatenate(([1], X_test[i])))) == Y_test[i])

print(correct / X_test.shape[0])
print(W)
