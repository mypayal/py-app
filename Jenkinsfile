pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS=credentials('dockerhub')
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Salmankhan7798/python-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image and tag it appropriately
                    sh 'docker build -t salmankhan7798/twimbit .'
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
				sh 'docker push salmankhan7798/twimbit:latest'
			}
		}

        stage('Deploy Docker Image') {
            steps {
                script {
                    // Build the Docker image and tag it appropriately
                    sh 'docker run -d -p 80:80 salmankhan7798/twimbit'
                }
            }
        }

    }
}
