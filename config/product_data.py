class Product:
    def __init__(self, product_id, name, price, quantity, total):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.total = total

products = [
    Product(
        product_id=1,
        name="Blue Top",
        price="Rs. 500",
        quantity="1",
        total="Rs. 500"
    ),
    Product(
        product_id=2,
        name="Men Tshirt",
        price="Rs. 400",
        quantity="1",
        total="Rs. 400"
    )
]
