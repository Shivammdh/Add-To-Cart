pipeline{
  
  agent any
  
  stages{
    
    stage("Checkout"){
      steps {
                checkout([$class: 'GitSCM', branches: [[name: 'main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/Shivammdh/Add-To-Cart.git']]])
            }
    }
      stage("Build"){
        steps {
                git branch: 'main', url: 'https://github.com/Shivammdh/Add-To-Cart.git'
                
            }
        }
    stage("Install dependencies"){
      steps {
        sh 'pip install -r requirements.txt'
      }
    }
      stage("Test"){
        steps{
          sh 'python3 -m Tests.maintest'
            }
        }
    }
}
      
      
      
