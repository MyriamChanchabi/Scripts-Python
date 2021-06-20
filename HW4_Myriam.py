import tensorflow as tf
from tensorflow import keras

import numpy as np
import matplotlib.pyplot as plt

fashion_mnist=keras.datasets.fashion_mnist
(train_images,train_labels),(test_images,test_labels)=fashion_mnist.load_data()

class_names=['tshirt/top','trouser','pullover','dress','coat','sandal','shirt','sneaker','bag','ankle boot']
train_images=train_images/255.0
test_images=test_images/255.0

model=keras.Sequential([keras.layers.Flatten(input_shape=(28,28)), keras.layers.Dense(128,activation=tf.nn.relu),keras.layers.Dense(10,activation=tf.nn.softmax)])

model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])

model.fit(train_images,train_labels,epochs=10)

test_loss,test_acc=model.evaluate(test_images,test_labels)
print('Test accuracy:',test_acc)
predictions =model.predict(test_images)

print("Prediction for [1088] image",predictions[1088])
print("Prediction class name:",class_names[np.argmax(predictions[1088])])
print('Test image true class name:', class_names[test_labels[1088]])

plt.figure()
plt.imshow(test_images[1088])
plt.colorbar()
plt.grid(False)
plt.show()