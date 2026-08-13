cache = {}

def get_user(user_id):
    if user_id not in cache:
        cache[user_id] = db.query(user_id)
    return cache[user_id]
