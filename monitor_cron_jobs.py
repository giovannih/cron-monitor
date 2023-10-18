import psycopg2
from datetime import datetime

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

    try:
        cursor.execute(query)
        records = cursor.fetchall()
        for record in records:
            job_name, is_online = record
            if not is_online:
                print(f'Job Name: {job_name}, Status: Offline')

    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    check_cron_jobs_status()

