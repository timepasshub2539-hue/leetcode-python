# s = {[1, 2]} -> error, lists are unhashable
s = {(1, 2)}  # tuples work instead
