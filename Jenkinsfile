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
      stage("Test"){
        step{
          sh 'python3 -m Tests.maintest'
            }
        }
    }
}
      
      
      
