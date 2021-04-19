import psycopg2

def create_db_connection():
    connection = psycopg2.connect(
                    database="team-3-group-project",
                    user="root", 
                    password="password", 
                    host="172.18.0.3", 
                    port="5432"
                    ) 
    return connection