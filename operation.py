import sqlite3
def search_contacts(name):
    a = 0
    b = 0

    conn = sqlite3.connect("phonebook.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM contacts WHERE names LIKE '%{name}%'")
    contact = cursor.fetchall()
    return contact




def list_names():
    conn = sqlite3.connect("phonebook.db")
    cursor = conn.cursor()

    cursor.execute("""SELECT * FROM contacts ORDER BY names""")
    contact = cursor.fetchall()
    return contact

def new_contact(name, number, email):
    conn = sqlite3.connect("phonebook.db")
    cursor = conn.cursor()

    cursor.execute(f"SELECT count(names) FROM contacts WHERE names LIKE '%{name}&'")
    check = cursor.fetchall()

    for row in check:
        for column in row:
            check = column
            break
    if check == 0:
        pass
    else:
        return "exists"
    cursor.execute(f"INSERT INTO contacts ('names', 'numbers', 'email') VALUES ('{name}', '{number}', '{email}')") 
    conn.commit()
    return "saved"

def delete_contact(name):
    conn = sqlite3.connect("phonebook.db")
    cursor = conn.cursor()
    check = cursor.execute(f"SELECT count(names) FROM contacts WHERE names LIKE '{name}'")

    for row in check:
        for column in row:
            check = column
            break

    if check == 0:
        return "nocontact"
    else:
        
        cursor.execute(f"DELETE FROM contacts WHERE names LIKE '{name}'")
        conn.commit()
        return "deleted"
    