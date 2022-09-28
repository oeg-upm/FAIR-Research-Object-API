import uuid, sqlite3 as sql, sys
from werkzeug.security import generate_password_hash, check_password_hash



def signup():
    if (len(sys.argv) != 3):
      print("Please enter the correct number of arguments. This program only takes two parameters, a username and a password in this same order.")
      return -1
      
    
    conn = sql.connect("./Database/enrrichmentDB.db")
    cursor = conn.cursor()
                   
    username = sys.argv[1]
    userpassword = generate_password_hash(sys.argv[2], method= 'sha256')
    id = str(uuid.uuid4())
    instruction = f"SELECT * FROM users WHERE username = '{username}'"
    result = cursor.execute(instruction).fetchone()
    if (result):
          print("The username already exists. Please try with another username.")
          return -1
    instruction = f"INSERT INTO users VALUES ('{id}','{username}','{userpassword}', 0)"
    cursor.execute(instruction)
    
    conn.commit()
    conn.close()
    print("User was created successfully!")
    return 1
  
#entry_dict = {'username':'NEW_USERNAME','userpassword':'NEW_PASSWORD'}

 
if __name__ == "__main__":
  
  signup()


  
  
  
