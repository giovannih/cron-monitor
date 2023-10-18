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
                    def scriptPath = "${WORKSPACE}/check_cron_jobs.py"
                    sh "python ${scriptPath}"
                }
            }
        }

        stage('Send Email Notifications') {
            steps {
                script {
                    // Check the status of your jobs and send email notifications if needed
                    if (check_cron_jobs_status()) {
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
