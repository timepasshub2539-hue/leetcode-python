def add(item, cart=[]):
    cart.append(item)
    return cart

# fix:
def add(item, cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart
