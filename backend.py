import sqlite3


def connect():
    conn = sqlite3.connect("hotel1.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS hotel1 (id INTEGER PRIMARY KEY, name text, address text, phone_number integer, no_of_days integer ,room_type text, total integer )")
    conn.commit()
    conn.close()


def insert(name, address, phone_number, no_of_days, room_type, total):
    from backend import calculation
    conn = sqlite3.connect("hotel1.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO hotel1 VALUES (NULL,?,?,?,?,?,?)", (name, address,
                                                                 phone_number, no_of_days, room_type, calculation(no_of_days, room_type)))
    conn.commit()
    conn.close()
    view()


def view():
    conn = sqlite3.connect("hotel1.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM hotel1")
    rows = cur.fetchall()
    conn.close()
    return rows


def search(name="", address="", phone_number="", room_type="", no_of_days="", total=""):
    conn = sqlite3.connect("hotel1.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM hotel1 WHERE name=? and address=? and phone_number=? and room_type=? or  no_of_days=? or  total=?",
                (name, address, phone_number, room_type, no_of_days, total))
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(id):
    conn = sqlite3.connect("hotel1.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM hotel1 WHERE id=?", (id,))
    conn.commit()
    conn.close()


def update(id, name, address, phone_number, room_type, no_of_days, total):
    from backend import calculation
    conn = sqlite3.connect("hotel1.db")
    cur = conn.cursor()
    cur.execute("UPDATE hotel1 SET name=?, address=?, phone_number=?, room_type=? ,no_of_days=? , total=? WHERE id=?",
                (name, address, phone_number, room_type, no_of_days, calculation(no_of_days, room_type), id))
    conn.commit()
    conn.close()


def calculation(no_of_days, room_type):
    if room_type == ("normal" or "NORMAL"):
        total = int(no_of_days)*1800
        return total
    elif room_type == ("king" or "KING"):
        total = int(no_of_days)*2400
        return total
    elif room_type == ("delux" or "DELUX"):
        total = int(no_of_days)*3500
        return total


connect()
