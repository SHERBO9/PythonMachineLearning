
import psycopg2.extras


DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASS = "0912"
DB_HOST = "localhost"
DB_PORT = "3600"

try:
    conn = psycopg2.connect(database=DB_NAME,
                            user=DB_USER,
                            password=DB_PASS,
                            host=DB_HOST,
                            port=DB_PORT)

    print("Database connected succesfully")

except:
    print("Database not connected")





