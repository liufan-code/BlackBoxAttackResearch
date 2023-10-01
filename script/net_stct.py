import tensorflow as tf

# DNN

model = tf.keras.Sequential()

model.add(tf.keras.layers.Dense(128, activation='relu', input_dim=10))
model.add(tf.keras.layers.Dense(128, activation='relu'))
model.add(tf.keras.layers.Dense(128, activation='relu'))
model.add(tf.keras.layers.Dense(2, activation='softmax'))

model.compile(optimizer="adam",
              loss="binary_crossentropy",
              metrics=["acc"])
model.summary()

# CNN
model = tf.keras.Sequential()

model.add(tf.keras.layers.Conv1D(100, 2, padding='valid', activation='relu', input_shape=(10,1)))
model.add(tf.keras.layers.MaxPool1D(pool_size=2))
model.add(tf.keras.layers.Conv1D(100, 2, padding='valid', activation='relu'))
model.add(tf.keras.layers.MaxPool1D(pool_size=2))
model.add(tf.keras.layers.Dropout(0.25))
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dropout(0.5))
model.add(tf.keras.layers.Dense(100, activation='relu'))
model.add(tf.keras.layers.Dense(2, activation='softmax'))

model.compile(optimizer="adam",
              loss="binary_crossentropy",
              metrics=["acc"])
model.summary()

# Simple RNN

model = tf.keras.Sequential()

model.add(tf.keras.layers.SimpleRNN(128, activation='tanh', return_sequences=True, input_shape=(10,1)))
model.add(tf.keras.layers.SimpleRNN(128, activation='tanh', return_sequences=True))
model.add(tf.keras.layers.SimpleRNN(128, activation='tanh'))
model.add(tf.keras.layers.Dense(1, activation='sigmoid'))

model.compile(optimizer="rmsprop",
              loss="binary_crossentropy",
              metrics=["acc"])
model.summary()

# LSTM

model = tf.keras.Sequential()

model.add(tf.keras.layers.LSTM(128, activation='tanh', return_sequences=True, input_shape=(10,1)))
model.add(tf.keras.layers.LSTM(128, activation='tanh', return_sequences=True))
model.add(tf.keras.layers.LSTM(128, activation='tanh'))
model.add(tf.keras.layers.Dense(2, activation='softmax'))

model.compile(optimizer="rmsprop",
              loss="binary_crossentropy",
              metrics=["acc"])
model.summary()

# GRU

model = tf.keras.Sequential()

model.add(tf.keras.layers.GRU(128, activation='tanh', return_sequences=True, input_shape=(10,1)))
model.add(tf.keras.layers.GRU(128, activation='tanh', return_sequences=True))
model.add(tf.keras.layers.GRU(128, activation='tanh'))
model.add(tf.keras.layers.Dense(1, activation='sigmoid'))

model.compile(optimizer="rmsprop",
              loss="binary_crossentropy",
              metrics=["acc"])
model.summary()