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


def best_promo(order):
    promos = [fidelity_promo, bulk_item_promo, large_order_promo]
    return max(promo(order) for promo in promos)
