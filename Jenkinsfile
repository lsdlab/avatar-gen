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
    stage('notification') {
      steps {
        slackSend(token: 'UZFyrMluz93IDFj4kCtjoEPH', teamDomain: 'https://breakwire.slack.com', message: 'jenkins build finished', baseUrl: 'https://breakwire.slack.com/services/hooks/jenkins-ci/', botUser: true)
      }
    }
  }
}