pipeline {
    agent any
    
    stages {
        stage('Build Docker Image') {
            steps {
                
                    bat "docker build -t DKImage ."
                
            }
        }

        stage('Run Docker Container') {
            steps {
                
                    bat "docker run --rm DKImage"
                
                
            }
        }
    }
}