while True:
    print("Калькулятор")
    print("1. Додавання")
    print("2. Віднімання")
    print("3. Множення")
    print("4. Ділення")
    print("5. Вихід")

    choice = input("Оберіть дію (1/2/3/4/5): ")

    if choice == '1':
        num1 = float(input("Введіть перше число: "))
        num2 = float(input("Введіть друге число: "))
        result = num1 + num2

    elif choice == '2':
        num1 = float(input("Введіть перше число: "))
        num2 = float(input("Введіть друге число: "))
        result = num1 - num2

    elif choice == '3':
        num1 = float(input("Введіть перше число: "))
        num2 = float(input("Введіть друге число: "))
        result = num1 * num2

    elif choice == '4':
        num1 = float(input("Введіть перше число: "))
        num2 = float(input("Введіть друге число: "))
        if num2 == 0:
            result = "Помилка! Ділення на 0"
        else:
            result = num1 / num2

    elif choice == '5':
        break

    print(f"Результат: {result}")