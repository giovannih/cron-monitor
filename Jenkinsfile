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
                    def workspacePath = pwd()
                    // Run your monitoring script
                    sh "python ${workspacePath}/monitor_cron_jobs.py"
                }
            }
        }

        stage('Send Email Notifications') {
            steps {
                script {
                    // Check the status of your jobs and send email notifications if needed
                    if (jobIsOffline) {
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
