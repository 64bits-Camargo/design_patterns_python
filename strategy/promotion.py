def fidelity_promo(order):
    discount = 0
    if order.customer.fidelity_points >= 1000:
        discount = order.subtotal * 0.05
    return discount


def bulk_item_promo(order):
    discount = 0
    for product in order.products:
        if product.quantity >= 20:
            discount += product.total * 0.1
    return discount


def large_order_promo(order):
    discount = 0
    distinct_products = list(set(order.products))
    if len(distinct_products) >= 10:
        discount = order.subtotal * 0.07
    return discount


promos = [globals()[name] for name in globals()
          if name.endswith('_promo') and name != 'best_promo']


def best_promo(order):
    return max(promo(order) for promo in promos)
