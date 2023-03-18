# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory to /app
# RUN pip install tensorflow_intel
# RUN pip install tensorflow
# RUN pip install numpy
# RUN pip install Flask
WORKDIR /app

# RUN pip install -r requirements.txt
# Copy the current directory contents into the container at /app

COPY . /app
COPY ./templates/index.html templates/
COPY ./static/style.css static/

# Install any needed packages specified in requirements.txt
RUN pip install -r /app/requirements.txt

# Expose port 5000 for the Flask app
EXPOSE 5000

COPY sentiment_model.h5 sentiment_model.h5
# Run app.py when the container launches
CMD ["python", "app.py"]
