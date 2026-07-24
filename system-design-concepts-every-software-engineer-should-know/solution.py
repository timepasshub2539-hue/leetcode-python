if cache.has(key):
    return cache.get(key)
result = slow_database_query(key)
cache.set(key, result)
return result
