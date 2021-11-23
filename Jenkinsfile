pipeline { 
agent any
    stages {
        stage('clone the repository') {
            steps {
                git 'https://github.com/pranu2502/jenkins-demo'
            }
        }
        stage('exec main') {
            steps {
		sh "chmod u+x prog.py"
                sh "python3 prog.py"
            }
        }
     stage('run tests') {
            steps {
		sh "chmod u+x test.py"
                sh "python3 test.py"
            }
        }
    }
    post {  
      always {  
          echo 'This will always run'  
      }  
      success {  
          mail bcc: '', body: "<b>Example</b><br>Project: ${env.JOB_NAME} <br>Build Number: ${env.BUILD_NUMBER} <br> URL de build: ${env.BUILD_URL}", cc: '', charset: 'UTF-8', from: '', mimeType: 'text/html', replyTo: '', subject: " CI Success: Project name -> ${env.JOB_NAME}", to: "spranavreddy25@gmail.com";  
      } 
      failure {  
          mail bcc: '', body: "<b>Example</b><br>Project: ${env.JOB_NAME} <br>Build Number: ${env.BUILD_NUMBER} <br> URL de build: ${env.BUILD_URL}", cc: '', charset: 'UTF-8', from: '', mimeType: 'text/html', replyTo: '', subject: "ERROR CI: Project name -> ${env.JOB_NAME}", to: "spranavreddy25@gmail.com";  
      }  
      unstable {  
          echo 'This will run only if the run was marked as unstable'  
      }  
      changed {  
          echo 'This will run only if the state of the Pipeline has changed'  
          echo 'For example, if the Pipeline was previously failing but is now successful'  
         }  
     } 
}
