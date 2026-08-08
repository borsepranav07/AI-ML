# Apply percentage discount
def apply_discount(price, percent):

    discount_amount = price * percent / 100

    return price - discount_amount


# Flat discount of 50
def flat_discount(price):

    return price - 50