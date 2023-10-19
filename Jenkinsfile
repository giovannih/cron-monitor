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
                    def scriptOutput = bat(script: "python ${scriptPath}", returnStdout: true).trim()
                    echo "Python Script Output:\n${scriptOutput}"

                    // Parse the JSON output from the Python script
                    def jsonData = readJSON text: scriptOutput
                    def offlineJobs = jsonData as List<String>

                    // Iterate over offline jobs
                    for (def jobName : offlineJobs) {
                        echo "Offline Job: ${jobName}"
                    }

                    // Store the email body
                    def emailBody = jsonData as String
                }
            }
        }

        stage('Send Email Notifications') {
            steps {
                script {
                    if (emailBody) {
                        withCredentials([usernamePassword(credentialsId: 'gmail', usernameVariable: 'SMTP_USERNAME', passwordVariable: 'SMTP_PASSWORD')]) {

                            emailext(
                                subject: 'CRON Jobs Status',
                                body: emailBody,
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
