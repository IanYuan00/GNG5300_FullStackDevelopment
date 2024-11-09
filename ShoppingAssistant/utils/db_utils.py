import sqlite3

def init_db():
    conn = sqlite3.connect('db/products.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            name TEXT,
            category TEXT,
            price REAL,
            stock INTEGER,
            description TEXT
        )
    ''')

    products = [
        ("Smartphone", "Electronics", 699.99, 10, "Latest model with high-speed processor"),
        ("Laptop", "Electronics", 1199.99, 5, "Powerful laptop with 16GB RAM"),
        ("Headphones", "Accessories", 199.99, 20, "Noise-cancelling over-ear headphones"),
        ("Coffee Maker", "Home Appliances", 49.99, 15, "Brew fresh coffee at home"),
    ]

    cursor.executemany('INSERT INTO products (name, category, price, stock, description) VALUES (?, ?, ?, ?, ?)', products)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
