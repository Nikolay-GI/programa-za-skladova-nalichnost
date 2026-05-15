import json


class InventoryManager:
    def __init__(self, filename="inventory.json"):
        self.filename = filename
        self.products = []
        self.load_products()

    def load_products(self):
        # Зареждане от файл
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                self.products = json.load(file)
        except FileNotFoundError:
            self.products = []
        except json.JSONDecodeError:
            print("Файлът е повреден.")
            self.products = []

    def save_products(self):
        # Запис във файл
        try:
            with open(self.filename, "w", encoding="utf-8") as file:
                json.dump(self.products, file, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Грешка при запис: {e}")

    def add_product(self, name, quantity, price, category):
        # Добавяне на продукт
        if name.strip() == "":
            print("Името не може да е празно.")
            return

        try:
            quantity = int(quantity)
            price = float(price)
        except ValueError:
            print("Количество и цена трябва да са числа.")
            return

        product = {
            "name": name,
            "quantity": quantity,
            "price": price,
            "category": category
        }

        self.products.append(product)
        self.save_products()
        print("Продуктът е добавен.")

    def show_products(self):
        # Показване на всички продукти
        if len(self.products) == 0:
            print("Няма продукти.")
            return

        for i, product in enumerate(self.products, start=1):
            self.print_product(i, product)

    def print_product(self, index, product):
        print(f"\nПродукт №{index}")
        print(f"Име: {product['name']}")
        print(f"Количество: {product['quantity']}")
        print(f"Цена: {product['price']}")
        print(f"Категория: {product['category']}")

    def delete_product(self, number):
        # Изтриване
        if number < 1 or number > len(self.products):
            print("Невалиден номер.")
            return

        removed = self.products.pop(number - 1)
        self.save_products()
        print(f"Изтрит продукт: {removed['name']}")

    def update_quantity(self, number, new_quantity):
        # Промяна на количество
        try:
            new_quantity = int(new_quantity)
        except ValueError:
            print("Невалидно число.")
            return

        if number < 1 or number > len(self.products):
            print("Невалиден номер.")
            return

        self.products[number - 1]["quantity"] = new_quantity
        self.save_products()
        print("Количество обновено.")

    def search_product(self, keyword):
        # Търсене
        results = []

        for product in self.products:
            if keyword.lower() in product["name"].lower():
                results.append(product)

        if not results:
            print("Няма намерени продукти.")
            return

        for i, product in enumerate(results, start=1):
            self.print_product(i, product)

    def filter_by_category(self, category):
        # Филтриране
        results = []

        for product in self.products:
            if product["category"].lower() == category.lower():
                results.append(product)

        if not results:
            print("Няма продукти в тази категория.")
            return

        for i, product in enumerate(results, start=1):
            self.print_product(i, product)

    def sort_by_price(self):
        # Сортиране по цена
        self.products.sort(key=lambda x: x["price"])
        self.save_products()
        print("Сортирано по цена.")

    def sort_by_quantity(self):
        # Сортиране по количество
        self.products.sort(key=lambda x: x["quantity"])
        self.save_products()
        print("Сортирано по количество.")

    def show_statistics(self):
        # Статистика
        total_products = len(self.products)
        total_quantity = 0
        total_value = 0

        for product in self.products:
            total_quantity += product["quantity"]
            total_value += product["quantity"] * product["price"]

        print("\n--- Статистика ---")
        print(f"Общо продукти: {total_products}")
        print(f"Общо количество: {total_quantity}")
        print(f"Обща стойност: {total_value:.2f} лв.")