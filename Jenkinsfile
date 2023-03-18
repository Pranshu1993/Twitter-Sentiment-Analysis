pipeline {
    environment {
        
        def imageName = "akhilesh3796/sentiment_app:v1-${env.BRANCH_NAME}-${env.BUILD_ID}"
        DOCKERHUB_CREDENTIALS=credentials('dockerhub-sentiment')

    }

    agent any 
        stages {

            stage("Build the Docker Image") {
                steps{
                    script {
                        sh "docker build -t ${imageName} ."
                    }
                }
            }
        
            stage("Push Image to the Docker Registry") {
                steps{
                    script {
                        sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                        sh "docker push ${imageName}"
                    }
                }
            }
             stage ('Remove Previous App Container') {
                steps {
                    echo 'Hello, '

                    sh '''#!/bin/bash
                        echo "START"
                        for id in $(docker ps -q)
                            do
                                echo "stopping container ${id}"
                                docker stop "${id}"
                                echo "DONE"
                            done
                    '''
                }
            }                  
            stage("Deploy New App Container on VM") {
                when{
                        branch 'master'
                    }
                steps{
                    script {
                        sh "docker pull ${imageName}"
                        sh "docker run -dt -p 80:5000 ${imageName}"
                    }
                }
            }
            
        }

}
