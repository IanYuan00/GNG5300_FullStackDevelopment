import sqlite3

def search_product(query):
    conn = sqlite3.connect('db/products.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE name LIKE ?", ('%' + query + '%',))
    result = cursor.fetchall()
    conn.close()
    return result

def recommend_products(category):
    conn = sqlite3.connect('db/products.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE category = ?", (category,))
    recommendations = cursor.fetchall()
    conn.close()
    return recommendations
