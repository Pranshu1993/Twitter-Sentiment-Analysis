
from flask import Flask, request, render_template,url_for
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences


# Load pre-trained sentiment analysis model
model = tf.keras.models.load_model('sentiment_model.h5')
tokenizer = Tokenizer(num_words=10000)

# Define sentiment labels
sentiment_labels = ['very sad', 'sad', 'neutral', 'happy', 'very happy']

# Initialize Flask app
app = Flask(__name__)

# Define the route for the home page
@app.route('/')
def home():
    return render_template('index.html', sentiment=None)

# Define the route for sentiment prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Check if clear button was clicked
    if 'clear-btn' in request.form:
        print("Clear button clicked!")
        # Clear the sentiment output
        return render_template('index.html', sentiment=None)
    else:
        # Get the input text from the form
        input_text = request.form['text']

        # Predict sentiment for the input text
        sentiment = predict_sentiment(input_text)

        # Return the sentiment to the web page
        return render_template('index.html', sentiment=sentiment)

def predict_sentiment(input_text):
    # Preprocess the input text
    sequences = tokenizer.texts_to_sequences([input_text])
    padded_sequences = pad_sequences(sequences, maxlen=100)

    # Use model to predict sentiment scores for the input
    score = model.predict(padded_sequences)[0]
    argmax_score = np.argmax(score)
    sentiment = sentiment_labels[argmax_score]

    return sentiment

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0',port=5000)

