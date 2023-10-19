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
                    // Parse the JSON string to get the list of offline jobs
                    def offlineJobsList = readJSON text: offlineJobs

                    // Iterate over the offline jobs
                    for (jobName in offlineJobsList) {
                        echo "Offline Job: ${jobName}"
                    }
                    echo "Python script executed successfully"
                }
            }
        }

        stage('Send Email Notifications') {
            steps {
                script {
                    // Check if there are offline jobs
                    if (offlineJobsList) {                        // Construct the email body with offline job names
                        withCredentials([usernamePassword(credentialsId: 'gmail', usernameVariable: 'SMTP_USERNAME', passwordVariable: 'SMTP_PASSWORD')]) {
                          emailext(
                            subject: 'CRON Jobs Offline',
                            body: "The following CRON jobs are offline:\n${offlineJobsList.join('\n')}",
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
