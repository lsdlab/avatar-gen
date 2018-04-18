pipeline {
  agent {
    docker {
      image 'python:3.5.3'
    }

  }
  stages {
    stage('build') {
      steps {
        sh 'pip install --user chen -r requirements.txt'
        sh 'pytest'
      }
    }
  }
}