pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS=credentials('dockerhub')
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/mypayal/py-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image and tag it appropriately
                    sh 'docker build -t payalshahare/twimbit .'
                }
            }
        }
        
		stage('Docker Login') {

			steps {
				sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
			}
		}

		stage('Push Image') {

			steps {
				sh 'docker push payalshahare/twimbit:latest'
			}
		}

        stage('Deploy Docker Image') {
            steps {
                script {
                    // Build the Docker image and tag it appropriately
                    sh 'docker run -d -p 80:80 payalshahare/twimbit'
                }
            }
        }

    }
}
