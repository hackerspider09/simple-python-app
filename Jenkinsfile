pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'hackerspider09/jenkins-demo-python-app'
        IMAGE_TAG = "v${BUILD_NUMBER}"
        GITHUB_REPO = "https://github.com/hackerspider09/simple-python-app.git"
    }

    stages {
        stage('Checkout') {
            when {
                branch 'dev'
            }
            steps {
                echo "Checkout to branch..."
                git branch: 'dev', url: "${env.GITHUB_REPO}"
            }
        }
        stage('Build') {
            steps {
                echo "Building Docker Image..."
                sh "docker build -t ${env.DOCKER_IMAGE}:${env.IMAGE_TAG} ."
            }
        }
        stage('Test') {
            steps {
                echo "Running Tests..."
                sh "docker run --rm ${env.DOCKER_IMAGE}:${env.IMAGE_TAG} python3 -m pytest tests.py"
            }
        }
        stage('Push') {
            steps {
                echo "Pushing Docker image with tag:${env.IMAGE_TAG}"
                withCredentials([usernamePassword(credentialsId: 'dockerhub', passwordVariable: 'DOCKERHUB_PASS', usernameVariable: 'DOCKERHUB_USER')]) {
                    sh "docker login -u ${DOCKERHUB_USER} -p ${DOCKERHUB_PASS}"
                    sh "docker push ${env.DOCKER_IMAGE}:${env.IMAGE_TAG}"
                    sh "docker logout"
                }
            }
        }
    }
}