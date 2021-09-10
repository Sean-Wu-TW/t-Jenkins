pipeline {
    agent any

    stages {
        stage('test'){
            steps {
                echo 'hello'
                sh 'echo hello2'
                sh 'pip3 --version'
                sh 'python3 --version'
                echo 'start venv'
                sh 'source bin/activate'
                sh 'pip3 install requirements.txt'
                echo 'done.'
            }
        }
    }
}