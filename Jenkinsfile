pipeline {
  agent {
    docker {
      image 'python:3.5.3'
    }

  }
  stages {
    stage('build') {
      steps {
        sh 'pip install -r requirements.txt'
        sh 'pytest'
      }
    }
  }
}