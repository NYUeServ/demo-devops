#!groovy 

pipeline {
	agent any 

	environment {
		HOST = "ec2-54-175-216-183.compute-1.amazonaws.com"
	}

	stages {
		stage('Checkout') {
			steps {
				checkout scm
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
				timeout(time: 30, unit: 'SECONDS'){
	                input(message:'Are you sure you want to deploy to Production?')
	            }
				echo "Deploying to ..."
				// TODO: Deploy steps
				// copy files to EC2 Host
				// sh "./run.sh"
			}
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