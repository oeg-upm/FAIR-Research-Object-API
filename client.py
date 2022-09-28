import requests, json, API_Server_v2, uuid
from flask import jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3 as sql




def signup(entry_dict:dict):
    conn = sql.connect("./Database/enrrichmentDB.db")
    cursor = conn.cursor()
                   
    username = entry_dict.get("username")
    userpassword = generate_password_hash(entry_dict.get("userpassword"), method= 'sha256')
    id = str(uuid.uuid4())
    instruction = f"INSERT INTO users VALUES ('{id}','{username}','{userpassword}', 0)"
    result = cursor.execute(instruction)
    
    conn.commit()
    conn.close()
   
    return 1
  
entry_dict = {'username':'egonzalez','userpassword':'pass_eg0nz@l3z'}

  
if __name__ == "__main__":
  
  signup(entry_dict)
  

  
  
  
