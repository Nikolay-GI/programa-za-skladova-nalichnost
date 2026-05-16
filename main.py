from models import InventoryManager


def menu():
    print("\n====== СИСТЕМА ЗА СКЛАДОВА ИНВЕНТАРИЗАЦИЯ ======")
    print("1. Добави продукт")
    print("2. Покажи всички продукти")
    print("3. Изтрий продукт")
    print("4. Обнови количество")
    print("5. Търси продукт")
    print("6. Филтрирай по категория")
    print("7. Сортирай по цена")
    print("8. Сортирай по количество")
    print("9. Статистика")
    print("0. Изход")


def read_number():
    try:
        return int(input("Въведи номер: "))
    except ValueError:
        print("Невалидно число.")
        return None


def main():
    manager = InventoryManager()

    while True:
        menu()
        choice = input("Избери опция: ")

        if choice == "1":
            name = input("Име: ")
            quantity = input("Количество: ")
            price = input("Цена: ")
            category = input("Категория: ")
            manager.add_product(name, quantity, price, category)

        elif choice == "2":
            manager.show_products()

        elif choice == "3":
            manager.show_products()
            number = read_number()
            if number:
                manager.delete_product(number)

        elif choice == "4":
            manager.show_products()
            number = read_number()
            if number:
                new_quantity = input("Ново количество: ")
                manager.update_quantity(number, new_quantity)

        elif choice == "5":
            keyword = input("Търси: ")
            manager.search_product(keyword)

        elif choice == "6":
            category = input("Категория: ")
            manager.filter_by_category(category)

        elif choice == "7":
            manager.sort_by_price()

        elif choice == "8":
            manager.sort_by_quantity()

        elif choice == "9":
            manager.show_statistics()

        elif choice == "0":
            print("Изход...")
            break

        else:
            print("Невалидна опция.")


if __name__ == "__main__":
    main()