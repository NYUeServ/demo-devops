#!groovy 

pipeline {
	agent any 

	environment {
		HOST = "ec2-54-175-216-183.compute-1.amazonaws.com"
		DEPLOY_DIR = "demo-devops/"
		TMP_DIR = ".tmp/"
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

		stage('Prepare for Deployment') {
			steps {
				sh "mkdir $TMP_DIR"
				sh "cp -r . $TMP_DIR"
				sh "mv $TMP_DIR $DEPLOY_DIR"
				sh "rm -rf $DEPLOY_DIR/.git"
			}
		}

		stage('Deploy') {
			steps {
				timeout(time: 30, unit: 'SECONDS'){
	                input(message:'Are you sure you want to deploy to Production?')
	            }
				echo "Deploying to $HOST"
				sh "scp -r $DEPLOY_DIR $HOST:/home/jenkins/"
				sh "ssh $HOST -t cd $DEPLOY_DIR & ./run.sh"
			}
		}

		stage('Clean Up') {
			steps { 
				echo "Cleaning up"
				sh "rm -rf $DEPLOY_DIR"
			}
		}
	}

	post {
		always {
			echo "Job finished"
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