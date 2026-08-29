def get_page(items, page, size):
    assert page >= 1, "pages start at 1"
    start = (page - 1) * size
    return items[start:start+size]
