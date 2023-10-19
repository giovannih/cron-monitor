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
                    def scriptPath = "${WORKSPACE}\\check_cron_jobs_status.py"
                    def scriptOutput = bat(script: "python ${scriptPath}", returnStatus: true, returnStdout: true)
                    if (scriptOutput != 0) {
                        // The script ran successfully
                        offlineJobs = scriptOutput.readLines()
                    } else {
                        error("Error running the script.")
                    }
                }
            }
        }

        stage('Send Email Notifications') {
            steps {
                script {
                    if (offlineJobs) {
                        // Iterate over the offline jobs and print them
                        for (jobName in offlineJobs) {
                            echo "Offline Job: ${jobName}"
                        }
                        withCredentials([usernamePassword(credentialsId: 'gmail', usernameVariable: 'SMTP_USERNAME', passwordVariable: 'SMTP_PASSWORD')]) {
                            emailext(
                                subject: 'CRON Jobs Offline',
                                body: "The following CRON jobs are offline:\n${offlineJobs.join('\n')}",
                                to: 'giovanni.harrius@sat.co.id',
                                replyTo: 'giovanni.harrius@sat.co.id'
                            )
                    }
                    }
                }
            }
        }
    }
}

