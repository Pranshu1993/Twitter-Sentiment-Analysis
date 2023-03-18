# Twitter Sentiment Analysis Application
This repository contains the code for a Twitter sentiment analysis application. The application extracts data from the Twitter API, cleans the data, and stores it in a MongoDB Atlas database. Then, a deep learning model is created using LSTM and RMSprop optimizer to perform sentiment analysis on the tweets. Once the model is created, a Docker image is created and uploaded to Docker Hub. The CI/CD pipeline is set up by integrating Jenkins with Docker and Git, and the web application is deployed on Docker.
Prerequisites

## To use this application, you will need the following tools:
1. Twitter API key
2. MongoDB Atlas account
3. Docker
4. Jenkins

## Installation and Usage Clone this repository:
1. git clone https://github.com/Akhilesh3796/Sentiment_analysis.git 
2. Set up your Twitter API key.
3. Set up your MongoDB Atlas account and set the connection details.
4. Create a Dockerfile.yaml and incorporate all the required dependancies.
4. Set up the CI/CD pipeline in Jenkins by following the steps in the Jenkinsfile.

## CI/CD pipeline (Jenkinsfile)
1. Build the Docker Image: 
    - This stage builds the Docker image of the application using the Dockerfile provided in the repository.
    - command: docker build -t {image_name} .
2. Push Image to the Docker Registry: 
    - This stage pushes the Docker image to Docker Hub registry using the Docker Hub credentials provided in the Jenkins credential store.
    - command: docker push {your-docker-username}/{Docker-image} 
3. Remove Previous App Container:
    - This stage stops and removes any previous instance of the application running on the virtual machine.
4. Deploy New App Container on VM: 
    - This stage deploys the new instance of the application by pulling the Docker image from the registry and running it on the virtual machine.

## Contributors
Akhilesh (@akhilesh3796),
Pranshu (@Pranshu1993),
Shreyash (@kopz96),
Rahul (@T3ch-miNer)

License
This project is licensed under the MIT License - see the LICENSE file for details.
