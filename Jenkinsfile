pipeline {
  agent none
  stages {
    stage('build') {
      steps {
        sh 'pip install -r requirements.txt'
        sh 'pytest'
      }
    }
  }
}