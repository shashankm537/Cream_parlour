import sqlite3

DB_NAME = "ice_cream_parlor.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def initialize_db():
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Flavors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        is_seasonal BOOLEAN
    );
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Ingredients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        flavor_id INTEGER,
        ingredient_name TEXT,
        quantity INTEGER,
        FOREIGN KEY (flavor_id) REFERENCES Flavors(id)
    );
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Allergens (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        description TEXT
    );
    """)
    
    conn.commit()
    conn.close()

initialize_db()
