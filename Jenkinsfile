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
      parallel {
        stage('slack') {
          steps {
            slackSend(token: 'UZFyrMluz93IDFj4kCtjoEPH', teamDomain: 'https://breakwire.slack.com', message: 'jenkins build finished', baseUrl: 'https://breakwire.slack.com/services/hooks/jenkins-ci/', botUser: true)
          }
        }
        stage('email') {
          steps {
            emailext(subject: 'jenkins build finished', body: 'jenkins build finished', attachLog: true, from: 'email@breakwire.me', mimeType: 'text/html', to: 'lsdvincent@gmail.com')
          }
        }
      }
    }
  }
}