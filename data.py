import sqlite3

db_path = 'pa.db'


# Connect to a database
def connect_db(path):
    conn = sqlite3.connect(path)
    # Convert tuples to dictionaries
    conn.row_factory = sqlite3.Row
    return (conn, conn.cursor())

# Read all pets by pet type
def read_pets_by_type(pet_type):
    conn, cur = connect_db(db_path)
    query = 'SELECT * FROM pets WHERE type=?'
    results = cur.execute(query, (pet_type,)).fetchall()
    conn.close()
    return results

# Read a pet given a pet id
def read_pet_by_id(pet_id):
    conn, cur = connect_db(db_path)
    query = 'SELECT * FROM pets WHERE id=?'
    result = cur.execute(query, (pet_id,)).fetchone()
    conn.close()
    return result

# Insert Pet Data to DB
def insert_pet(pet_data):
    conn, cur = connect_db(db_path)
    query = 'INSERT INTO pets (name, age, description, breed, url, type) VALUES (?,?,?,?,?,?)'
    values = (pet_data['name'],
              pet_data['age'],
              pet_data['description'],
              pet_data['breed'],
              pet_data['url'],
              pet_data['type'])
    cur.execute(query, values)
    conn.commit()
    conn.close()

# Delete a pet record
def delete_pet(pet_id):
    conn, cur = connect_db(db_path)
    query = 'DELETE FROM pets WHERE id=?'
    cur.execute(query, (pet_id,))
    conn.commit()
    conn.close()

# Update Pet Data from DB
def update_pet(pet_data):
    conn, cur = connect_db(db_path)
    query = 'UPDATE pets SET name=?, age=?, description=?, breed=?, url=?, type=? WHERE id=?'
    values = (pet_data['name'],
              pet_data['age'],
              pet_data['description'],
              pet_data['breed'],
              pet_data['url'],
              pet_data['type'],
              pet_data['id'])
    cur.execute(query, values)
    conn.commit()
    conn.close()
