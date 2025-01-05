import mysql.connector
from bcrypt import hashpw, gensalt
import uuid
def hash_password(password):
    hashed_password = hashpw(password.encode('utf-8'), gensalt())
    return hashed_password
def formatted_vnd(amount):
    return f"{amount:,.0f}".replace(",", ".")
def generate_numeric_id():
    raw_uuid = str(uuid.uuid4())
    numeric_id = int(''.join(filter(str.isdigit, raw_uuid)))
    return numeric_id % 10**12  

def user_exists(username):
    db_connection = mysql.connector.connect(
    host ='localhost',
    user ="root",
    password = "Anh@2005",
    database ="expense_tracker_ka"
    )
    cursor = db_connection.cursor()
    query = "SELECT COUNT(*) FROM users WHERE username = %s"
    cursor.execute(query, (username,))
    exists = cursor.fetchone()[0] > 0
    cursor.close()
    db_connection.close()
    return exists
def store_user_in_database(username, password,balance ):
    db_connection = mysql.connector.connect(
    host ='localhost',
    user ="root",
    password = "Anh@2005",
    database ="expense_tracker_ka"
)
    cursor = db_connection.cursor()
    hashed_password = hash_password(password)
    formatted_balance = formatted_vnd(balance)
    random_id = generate_numeric_id()
    query = "INSERT INTO users (random_id,username, password_hash,balance) VALUES (%s,%s, %s, %s)"
    values = (random_id, username, hashed_password,formatted_balance)
    try:
        cursor.execute(query, values)
        db_connection.commit()
        print("User stored successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        db_connection.close()