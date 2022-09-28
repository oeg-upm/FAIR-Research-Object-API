import sqlite3 as sql
def create_database():
    conn = sql.connect("./Database/enrrichmentDB.db")
    cursor = conn.cursor()                
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
    id text NOT NULL UNIQUE PRIMARY KEY,
    username text NOT NULL, 
    userpassword text NOT NULL,
    admin boolean DEFAULT 0)""")
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS jobs (
    job_id text NOT NULL, 
    original_name text NOT NULL, 
    client text NOT NULL, 
    ready boolean NOT NULL)""")
    conn.close()
    
    print("Database tables were created successfully!")
    return


    
if __name__ == "__main__":
    create_database()