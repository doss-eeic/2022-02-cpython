class Product:
    def __init__(self, name: str, price: int, weight: float) -> None:
        self.name = name
        self.price = price
        self.weight = weight

products = [
    Product("apple", 100, 12.2),
    Product("apple_watch", 50000, 123.4),
    Product("apple_juice", 400, 32.2),
    Product("grape", 120, 120.5),
    Product("orange_cake", 1000, 10.0),
]

sum_of_price = products \
    .filter(lambda p: "apple" in p.name) \
    .filter(lambda p: p.price <= 500) \
    .map(lambda p: p.weight) \
    .sum()
    
assert sum_of_price == 12.2 + 32.2