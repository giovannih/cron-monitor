import psycopg2
from datetime import datetime

# Establish a PostgreSQL connection
conn = psycopg2.connect(
    dbname="your_db_name",
    user="your_db_user",
    password="your_db_password",
    host="your_db_host"
)

cursor = conn.cursor()

# Define a function to check the job status
def check_job_status(job_name):
    query = "SELECT is_online, next_run FROM cron_jobs WHERE job_name = %s"
    cursor.execute(query, (job_name,))
    result = cursor.fetchone()

    if result:
        is_online, next_run = result
        current_time = datetime.now()

        if is_online and next_run <= current_time:
            return "Online"  # Job is online and next run time is in the past
        else:
            return "Offline"  # Job is offline or next run time is in the future
    else:
        return "Not Found"  # Job with that name not in the database

# Example usage
job_name = "your_job_name"
status = check_job_status(job_name)
print(f"Status of {job_name}: {status}")

conn.commit()
cursor.close()
conn.close()
