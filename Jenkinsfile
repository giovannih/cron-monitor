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
                    def scriptOutput = bat(script: "python ${scriptPath}", returnStatus: true, returnStdout: true)
                    // Capture the script's output for later use
                    currentBuild.description = scriptOutput
                }
            }
        }

        stage('Send Email Notifications') {
            steps {
                script {
                    // Get the captured script output
                    def scriptOutput = currentBuild.description

                    // Check if there are offline jobs
                    if (scriptOutput) {
                        // Split the output into a list of offline job names
                        def offlineJobsList = scriptOutput.split('\n').collect { it - "- " }

                        // Construct the email body with offline job names
                        def emailBody = "The following CRON jobs are offline:\n\n"
                        offlineJobsList.each { jobName ->
                            emailBody += "- $jobName\n"
                        }
                        withCredentials([usernamePassword(credentialsId: 'gmail', usernameVariable: 'SMTP_USERNAME', passwordVariable: 'SMTP_PASSWORD')]) {
                          emailext(
                            subject: 'CRON Jobs Offline',
                            body: emailBody,
                            to: 'giovanniharrius@gmail.com',
                            replyTo: 'giovanniharrius@gmail.com'
                            )  
                        }
                        // Send email notification
                        
                    }
                }
            }
        }
    }
}
