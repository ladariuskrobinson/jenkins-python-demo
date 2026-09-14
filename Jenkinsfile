pipeline {
    agent any
        // this tells jenkins to run the pipeline on any available agent such as Linux, Windows, or MacOS. You can also specify a specific agent if needed.
    environment {
        DOCKER_IMAGE = 'ladarius9/my-app:latest' // Define a Docker image name for deployment
        // Define environment variables here if needed
    }

    stages {
        
        stage('Build') {
            steps {
                sh 'python3 -m venv venv' // Create a virtual environment
                sh 'venv/bin/pip install -r requirements.txt' // Install dependencies from requirements.txt
                sh 'venv/bin/python -m py_compile app.py' // Compile the Python code to check for syntax errorsecho 'Building...'
                // Add build steps here, such as compiling code or running tests
            }
        }
        
        stage('Test') {
            steps {
                sh 'venv/bin/python -m pytest' // Run unit tests
                // Add test steps here, such as running unit tests or integration tests
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE .' // Build a Docker image for deployment
                // Add steps to build a Docker image or package the application
            }
        }
        
        stage('Push Docker Image') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub-credentials-id', 
                        usernameVariable: 'DOCKER_USERNAME', 
                        passwordVariable: 'DOCKER_PASSWORD'
                        )
                    ]) {
                        sh 'echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin' // Log in to Docker Hub
                        sh 'docker push $DOCKER_IMAGE' // Push the Docker image to Docker Hub
                }
                // Add steps to push the Docker image to a registry or repository
            }
        }

        stage('Deploy') {
            steps {
                sh 'venv/bin/python app.py' // Run the application (or add deployment steps)
                // Add deployment steps here, such as deploying to a server or cloud environment
            }
        }

    }
    
}