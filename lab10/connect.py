
import psycopg2
conn = psycopg2.connect( 
    host = "localhost",
    database = "postgres",
    user = "postgres",
    password = "postgres",
    port = 5432
)
cursor = conn.cursor()
conn.autocommit = True
cursor.execute("CREATE TABLE people (surename SERIAL PRIMARY KEY, name VARCHAR(50),  number INTEGER)")
conn.commit()

cursor.close()
conn.close()