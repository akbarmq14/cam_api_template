pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building Camera_api..'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing Camera_api..'
		sh 'python3 unitTest_cam_api.py' 
           }
        }
        stage('Deploy Stage') {
            steps {
                echo 'Deploying....'
		echo '...Finished exec...'
            }
        }
        stage('End') {
            steps {
                echo 'Ending Camera_api..'
            }
        }

    }
}
