import sqlite3

def get_all_pets():
    conn = sqlite3.connect('veterinaria.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, species, age FROM pets')
    pets = cursor.fetchall()
    conn.close()

    pet_list = []
    for pet in pets:
        pet_id, name, species, age = pet
        pet_list.append({
            "id": pet_id,
            "name": name,
            "species": species,
            "age": age
        })
    return pet_list

def get_pet_by_id(pet_id):
    conn = sqlite3.connect('veterinaria.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, species, age FROM pets WHERE id = ?', (pet_id,))
    pet = cursor.fetchone()
    conn.close()

    if pet:
        pet_id, name, species, age = pet
        return {
            "id": pet_id,
            "name": name,
            "species": species,
            "age": age
        }
    return None

def create_pet(name, species, age):
    conn = sqlite3.connect('veterinaria.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO pets (name, species, age) VALUES (?, ?, ?)', 
                   (name, species, age))
    conn.commit()
    pet_id = cursor.lastrowid
    conn.close()
    return pet_id

def update_pet(pet_id, name, species, age):
    conn = sqlite3.connect('veterinaria.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE pets SET name = ?, species = ?, age = ? WHERE id = ?', 
                   (name, species, age, pet_id))
    conn.commit()
    conn.close()

def delete_pet(pet_id):
    conn = sqlite3.connect('veterinaria.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM pets WHERE id = ?', (pet_id,))
    conn.commit()
    conn.close()