import psycopg2

def check_cron_jobs_status():
    # Database connection parameters
    db_params = {
        'database': 'postgres',
        'user': 'postgres',
        'password': '123456',
        'host': 'localhost',
        'port': '5432'
    }

    # Connect to the database
    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor()

    # Query to select job_name and is_online from the cron_jobs table
    query = "SELECT job_name, is_online FROM cron_jobs"

    # Create a list to store the names of offline jobs
    offline_jobs = []

    try:
        cursor.execute(query)
        records = cursor.fetchall()
        for record in records:
            job_name, is_online = record
            if not is_online:
                offline_jobs.append(job_name)  # Add the offline job name to the list

        # Check if there are offline jobs
        if offline_jobs:
            # Print the names of offline jobs
            print("The following CRON jobs are offline:")
            for job_name in offline_jobs:
                print(f'- {job_name}')
        else:
            print("All CRON jobs are online.")

    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    check_cron_jobs_status()
