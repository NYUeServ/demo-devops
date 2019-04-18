#!groovy 

pipeline {
	agent any 

	environment {
		HOST = "ec2-54-175-216-183.compute-1.amazonaws.com"
		DEPLOY_DIR = "demo-devops"
		TEST_DIR = "tests"
		commitChangeset = sh(returnStdout: true, script: 'git log -1 --pretty=%B')
	}

	stages {
		stage('Checkout') {
			steps {
				checkout scm
			}
		}

		stage('Prepare for Deployment') {
			steps {
				sh "mkdir $DEPLOY_DIR"
				sh "rsync -vaz --exclude=$DEPLOY_DIR . $DEPLOY_DIR"
				sh "rm -rf $DEPLOY_DIR/.git"
			}
		}

		stage('Deploy') {
			steps {
				//timeout(time: 30, unit: 'SECONDS'){
	                //input(message:'Are you sure you want to deploy to Production?')
	            //}
				echo "Deploying to $HOST"
				sh "scp -r $DEPLOY_DIR $HOST:/home/jenkins/"
				sh """
					# Just used this as a one-off to accept the host key on the first run.
             		ssh -o StrictHostKeyChecking=no $HOST /bin/true
					
					ssh $HOST chmod +x $DEPLOY_DIR/*.sh $DEPLOY_DIR/*.py
					ssh $HOST ./$DEPLOY_DIR/run.sh
				"""
			}
		}
	}
	
	post {
		always {
			echo "Job finished"

				echo "Starting Tests"
				sh label: '', script: '''curl https://api.ghostinspector.com/v1/tests/5ca7a0a436caaa1fcaabd839/execute/?apiKey=b96df7f3ed65abb075c6f3b3dfcf959c6e3daf4a&startUrl=http://ec2-54-175-216-183.compute-1.amazonaws.com:5000'''

			echo "Cleaning up"
			sh "rm -rf $DEPLOY_DIR $TEST_DIR"
			
		}
		success {
			slackSend channel: "#demo", 
			color: "good", 
				message: "Deployed application SUCCESS. \n ${commitChangeset} \n See ${env.JOB_NAME} ${env.BUILD_NUMBER} (<$BUILD_URL|Open>). \n WebApp deploy to <$HOST:5000> \n:yay:"
		}
		failure {
			slackSend channel: "#demo",
			color: "danger",
			message: "Deploy FAILED. \n ${GIT_COMMIT} \nSee ${env.JOB_NAME} ${env.BUILD_NUMBER} (<$BUILD_URL|Open>)"
		}
	}
}
