pipeline {
    agent any

    environment {
        
        APP_NAME = "TemperatureConverter"
    }

    stages {
        stage('Checkout') {
            steps {
                echo "Pulling latest code from repository..."
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo "Compiling the application..."
                
                echo "Application built successfully."
            }
        }

        stage('Test: Celsius to Fahrenheit') {
            when {
                anyOf {
                    branch 'push-1'
                    branch 'main'
                    branch 'master'
                }
            }
            steps {
                echo "Running unit tests for Celsius to Fahrenheit conversion (Push 1 Feature)..."
                
            }
        }

        stage('Test: Fahrenheit to Celsius') {
            when {
                anyOf {
                    branch 'push-2'
                    branch 'main'
                    branch 'master'
                }
            }
            steps {
                echo "Running unit tests for Fahrenheit to Celsius conversion (Push 2 Feature)..."
                
            }
        }

        stage('Security Scan') {
            steps {
                echo "Running static code analysis..."
                
            }
        }

        stage('Deploy Staging') {
            when {
                anyOf {
                    branch 'main'
                    branch 'master'
                }
            }
            steps {
                echo "Deploying the complete application to the Staging Environment..."
            }
        }
    }

    post {
        always {
            echo "Cleaning up workspace..."
            cleanWs()
        }
        success {
            echo "Pipeline completed successfully! Build is stable."
        }
        failure {
            echo "Pipeline failed. Please check the logs above for errors."
        }
    }
}

  
