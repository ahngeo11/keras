#다중 분류
import numpy as np

#sklearn boston
from sklearn.datasets import load_iris

#1.
dataset = load_iris()
x = dataset.data
y = dataset.target
print("shape of iris dataset : ", x.shape, y.shape)
#(150, 4)(150,)

# print(dataset.feature_names)
# print(dataset.DESCR)

#one-hot encoding
from tensorflow.keras.utils import to_categorical
y = to_categorical(y)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, 
    train_size=0.8, random_state=66)

#2.
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Dense, Input

model = Sequential()
model.add(Dense(10, activation='relu', input_shape=(4,)))
model.add(Dense(50))
model.add(Dense(20))
model.add(Dense(3, activation='softmax')) #다중분류 = softmax
#             라벨개수 (... one hot encoding)


#3.
#model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['acc'])
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['acc'])
model.fit(x_train, y_train, epochs=100, batch_size=1,
    verbose=1, validation_split=0.1)

#4.
loss = model.evaluate(x_test, y_test)
print("results : ", loss) #[categorical_crossentropy loss , accuarcy]

y_predict = model.predict(x_test)
print(y_test[:3])
print(y_predict[:3])

from sklearn.metrics import r2_score
R2 = r2_score(y_predict, y_test)
print("R2 : ", R2)