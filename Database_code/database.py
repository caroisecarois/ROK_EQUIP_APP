from sqlalchemy import text

def start_database(conn):
    try: 
        conn.execute(text('''CREATE TABLE IF NOT EXISTS materials (material_id INTEGER PRIMARY KEY, material_name VARCHAR(255))'''))
        conn.execute(text('''CREATE TABLE IF NOT EXISTS quality (quality_id INTEGER PRIMARY KEY, quality_name VARCHAR(255))'''))
        conn.execute(text('''INSERT OR IGNORE INTO materials (material_id, material_name) VALUES (1, 'Leather')'''))
        conn.execute(text('''INSERT OR IGNORE INTO materials (material_id, material_name) VALUES (2, 'Iron')'''))
        conn.execute(text('''INSERT OR IGNORE INTO materials (material_id, material_name) VALUES (3, 'Animal bone')'''))
        conn.execute(text('''INSERT OR IGNORE INTO materials (material_id, material_name) VALUES (1, 'Ebony')'''))
        conn.execute(text('''INSERT OR IGNORE INTO quality (quality_id, quality_name) VALUES (1, 'Normal')'''))
        conn.execute(text('''INSERT OR IGNORE INTO quality (quality_id, quality_name) VALUES (2, 'Advanced')'''))
        conn.execute(text('''INSERT OR IGNORE INTO quality (quality_id, quality_name) VALUES (1, 'Elite')'''))
        conn.execute(text('''INSERT OR IGNORE INTO quality (quality_id, quality_name) VALUES (1, 'Epic')'''))
        conn.execute(text('''INSERT OR IGNORE INTO quality (quality_id, quality_name) VALUES (1, 'Legendary')'''))
    except Exception as e:
        print(str(e))

def create_working_tables(conn):
    conn.execute(text('''CREATE TABLE IF NOT EXISTS mq (mq_id INTEGER PRIMARY KEY, material_id INTEGER FOREING KEY, quality_id INTEGER FOREIGN KEY,
                      quantity INTEGER)'''))

def insery_mq_table(mq_id, material_id, quality_id, quantity, conn):
    conn.execute(text('''INSERT OR IGNORE INTO mq (mq_id, material_id, quality_id, quantity) VALUES(?)''')(mq_id, material_id, quality_id, quantity))