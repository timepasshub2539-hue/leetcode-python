def get_price(id):
    return db.query(
      "SELECT price FROM items WHERE id=%s", id)

# no caching -- every call hits the DB
