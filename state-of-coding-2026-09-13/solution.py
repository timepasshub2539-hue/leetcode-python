# a typical example of the kind of bug that slips through
def get_discount(price, is_member):
    if is_member:
        return price * 0.9
    return price

# what a careful reviewer catches:
# negative price still "discounts" to a negative number —
# the ticket never said validate input, but production data will.
