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
                    def scriptPath = "${WORKSPACE}\\check_cron_jobs_status.py"
                    def offlineJobs = bat(script: "python ${scriptPath}", returnStatus: true, returnStdout: true).trim()
                    
                    // Parse the JSON string to get the list of offline jobs
                    def offlineJobsList = readJSON text: offlineJobs

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
                    // Get the captured script output
                    def scriptOutput = currentBuild.description
                    echo "Python Script Output: ${scriptOutput}"
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
                            body: "The following CRON jobs are offline: ${offlineJobsList.join('\n')}",
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
