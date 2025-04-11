import sqlite3

def get_all_appointments():
    conn = sqlite3.connect('veterinaria.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM appointments')
    appointments = cursor.fetchall()
    conn.close()
    return appointments

def get_appointments_by_pet(pet_id):
    conn = sqlite3.connect('veterinaria.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM appointments WHERE pet_id = ?', (pet_id,))
    appointments = cursor.fetchall()
    conn.close()
    return appointments

def create_appointment(date, reason, pet_id):
    conn = sqlite3.connect('veterinaria.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO appointments (date, reason, pet_id) VALUES (?, ?, ?)', 
                   (date, reason, pet_id))
    conn.commit()
    appointment_id = cursor.lastrowid
    conn.close()
    return appointment_id

def update_appointment(appointment_id, date, reason, pet_id):
    conn = sqlite3.connect('veterinaria.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE appointments SET date = ?, reason = ?, pet_id = ? WHERE id = ?', 
                   (date, reason, pet_id, appointment_id))
    conn.commit()
    conn.close()

def delete_appointment(appointment_id):
    conn = sqlite3.connect('veterinaria.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM appointments WHERE id = ?', (appointment_id,))
    conn.commit()
    conn.close()