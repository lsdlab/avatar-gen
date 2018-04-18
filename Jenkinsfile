pipeline {
  agent any
  stages {
    stage('deps') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }
    stage('test') {
      steps {
        sh 'pytest'
      }
    }
  }
}