def offlineJobs // Define offlineJobs at a higher scope

pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Monitor CRON Jobs') {
            steps {
                script {
                    def scriptPath = "${WORKSPACE}\\monitor_cron_jobs.py"
                    offlineJobs = bat(script: "python ${scriptPath}", returnStatus: true, returnStdout: true).trim()
                    
                    // Parse the output string into a list
                    def offlineJobsList = offlineJobs.tokenize('\n')

                    // Iterate over the offline jobs
                    for (jobName in offlineJobsList) {
                        echo "Offline Job: ${jobName}"
                    }
                }
            }
        }

        stage('Send Email Notifications') {
            steps {
                script {
                    if (offlineJobs) {
                        emailext(
                            subject: 'CRON Jobs Offline',
                            body: "The following CRON jobs are offline:\n${offlineJobs}",
                            to: 'giovanni.harrius@sat.co.id',
                            replyTo: 'giovanni.harrius@sat.co.id'
                        )
                    }
                }
            }
        }
    }
}
