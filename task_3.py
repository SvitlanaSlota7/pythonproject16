class Product:
    def __init__(self, product_type: str, name: str, price: float):
        self.type = product_type
        self.name = name
        self.price = price

class ProductStore:
    def __init__(self):
        # Структура: { "назва": {"product": obj, "amount": int, "revenue": float} }
        self.inventory = {}
        self.markup = 1.3  # націнка 30%

    def add(self, product: Product, amount: int):
        if amount <= 0:
            raise ValueError("Кількість має бути додатною")

        # Додаємо націнку
        product.price *= self.markup

        if product.name not in self.inventory:
            self.inventory[product.name] = {
                'product': product,
                'amount': amount,
                'revenue': 0.0  # Дохід по цьому товару
            }
        else:
            self.inventory[product.name]['amount'] += amount

    def sell_product(self, product_name: str, amount: int):
        if product_name not in self.inventory:
            raise ValueError(f"Товар '{product_name}' не знайдено")

        if self.inventory[product_name]['amount'] < amount:
            raise ValueError(f"Недостатньо '{product_name}' на складі")

        self.inventory[product_name]['amount'] -= amount
        sale_sum = self.inventory[product_name]['product'].price * amount
        self.inventory[product_name]['revenue'] += sale_sum

    def get_detailed_stats(self):
        total_income = 0
        print(f"{'Назва':<15} | {'Залишок':<10} | {'Дохід з товару':<15}")

        for name, data in self.inventory.items():
            amount = data['amount']
            revenue = data['revenue']
            total_income += revenue
            print(f"{name:<15} | {amount:<10} | {revenue:<15.2f}")

        print(f"ЗАГАЛЬНИЙ ДОХІД: {total_income:.2f}")

s = ProductStore()

p_pepsi = Product('Food', 'Pepsi', 1.5)
s.add(p_pepsi, 300)

p_shirt = Product('Sport', 'Football T-Shirt', 100)
p_laptop = Product('Electronics', 'MacBook', 2000)
p_soap = Product('Hygiene', 'Soap', 2.0)

s.add(p_shirt, 10)
s.add(p_laptop, 5)
s.add(p_soap, 50)

s.sell_product('Pepsi', 50)  # Продано 50 шт
s.sell_product('Football T-Shirt', 2)
s.sell_product('MacBook', 1)
s.sell_product('Soap', 10)

s.get_detailed_stats()