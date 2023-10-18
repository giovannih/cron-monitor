pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                // Use the "checkout" step to retrieve code from the VCS repository
                checkout scm
            }
        }

        stage('Monitor CRON Jobs') {
            steps {
                script {
                    def scriptPath = "${WORKSPACE}\\monitor_cron_jobs.py"
                    bat "python ${scriptPath}"
                }
            }
        }

        stage('Send Email Notifications') {
            steps {
                script {
                    // Call the Python script to check the job status
                    def scriptPath = "${WORKSPACE}\\monitor_cron_jobs.py"
                    def isJobOffline = bat(script: "python ${scriptPath}", returnStatus: true)

                    if (isJobOffline == 0) {
                        emailext(
                            subject: 'CRON Job Offline',
                            body: 'One or more CRON jobs are offline.',
                            to: 'giovanni.harrius@sat.co.id',
                            replyTo: 'giovanni.harrius@sat.co.id'
                        )
                    }
                }
            }
        }

    }
}
