FIDELITY_PERCENT_DISCOUNT = 0.05
BULK_ITEM_PERCENT_DISCOUNT = 0.1
LARGE_ORDER_PERCENT_DISCOUNT = 0.07

MIN_FIDELITY_POINTS_DISCOUNT = 1000
MIN_PRODUCTS_LARGE_DISCOUNT = 10
MIN_BULK_ITEM_DISCOUNT = 20


def fidelity_promo(order):
    discount = 0
    if order.customer.fidelity_points >= MIN_FIDELITY_POINTS_DISCOUNT:
        discount = order.subtotal * FIDELITY_PERCENT_DISCOUNT
    return discount


def bulk_item_promo(order):
    discount = 0
    for product in order.products:
        if product.quantity >= MIN_BULK_ITEM_DISCOUNT:
            discount += product.total * BULK_ITEM_PERCENT_DISCOUNT
    return discount


def large_order_promo(order):
    discount = 0
    distinct_products = list(set(order.products))
    if len(distinct_products) >= MIN_PRODUCTS_LARGE_DISCOUNT:
        discount = order.subtotal * LARGE_ORDER_PERCENT_DISCOUNT
    return discount


promos = [globals()[name] for name in globals()
          if name.endswith('_promo') and name != 'best_promo']


def best_promo(order):
    return max(promo(order) for promo in promos)
