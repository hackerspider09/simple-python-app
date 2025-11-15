pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'hackerspider09/jenkins-demo-python-app'
    }

    stages {
        stage('Checkout') {
            when {
                branch 'dev'
            }
            steps {
                git branch: 'dev', url: 'https://github.com/hackerspider09/simple-python-app.git'
            }
        }
        stage('Build') {
            steps {
                echo "Building Docker Image..."
            }
        }
        stage('Test') {
            steps {
                echo "Running Tests..."
            }
        }
        stage('Deploy') {
            steps {
                echo "Deploying Application..."
            }
        }
    }
}