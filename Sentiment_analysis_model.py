#Run THis after getiing extracting data
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split
import string

import extraction

# Load the dataset
data = pd.read_csv('sentiment_analysis.csv')

# # Preprocess the data
# tokenizer = Tokenizer(num_words=10000)
# tokenizer.fit_on_texts(data['tweet'].values)

# Convert the 'tweet' column to a list of strings
tweets = data['tweet'].astype(str)

data.dropna(axis=0, how='any', inplace=True)


# Convert the 'tweet' column to a list of strings
tweets = data['tweet'].astype(str).tolist()



# Create a tokenizer object
tokenizer = Tokenizer(num_words=10000, filters=string.printable)

# Fit the tokenizer on the tweets
tokenizer.fit_on_texts(data['tweet'].values)

X = tokenizer.texts_to_sequences(data['tweet'].values)
X = pad_sequences(X, maxlen=100)
y = pd.get_dummies(data['sentiment']).values

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build the model
model = Sequential()
model.add(Embedding(10000, 128, input_length=100))
model.add(LSTM(128, dropout=0.2, recurrent_dropout=0.2))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(6, activation='softmax'))

# Compile the model
model.compile(loss='categorical_crossentropy', optimizer='RMSprop', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=1, batch_size=64)

# Save the model
model.save('sentiment_model.h5')