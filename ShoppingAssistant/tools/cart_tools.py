cart = {}

def add_to_cart(product_id, quantity):
    if product_id in cart:
        cart[product_id] += quantity
    else:
        cart[product_id] = quantity
    return cart

def remove_from_cart(product_id):
    if product_id in cart:
        del cart[product_id]
    return cart

def view_cart():
    return cart
