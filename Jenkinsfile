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
                    echo "Python script executed successfully"
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
                        // Extract the list of offline job names from the script output
                        def offlineJobsList = scriptOutput.tokenize('-').collect { it.trim() }
                        offlineJobsList = offlineJobsList.findAll { it }

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
        post {
                always {
                    archiveArtifacts artifacts: 'output.log', allowEmptyArchive: true
                    }
            }
        }
    }
}
