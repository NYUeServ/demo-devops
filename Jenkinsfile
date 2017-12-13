#!groovy 

pipelines {
	agent any 

	stages {
		stage('Checkout') {
			steps {
				checkout scm
			}
		}
	}

	stage('Unit Tests') {
		steps {
			echo "Starting Tests"
			// TODO: Run unit tests on the updated code
		}
	}

	stage('Deploy') {
		steps {
			echo "Deploying to ..."
			// TODO: Deploy steps
		}
	}

	post {
		always {
			// junit '*.xml'
		}
		success {
			slackSend channel: "#demo", 
			color: "good", 
			message: "Deployed application SUCCESS. See ${env.JOB_NAME} ${env.BUILD_NUMBER} (<${env.BUILD_URL}|Open>)"
		}
		failure {
			slackSend channel: "#demo",
			color: "danger",
			message: "Deploy FAILED. See ${env.JOB_NAME} ${env.BUILD_NUMBER} (<${env.BUILD_URL}|Open>)"
		}
	}
}