def calc():
    print("=" * 30)
    print("\t Калькулятор")
    print("=" * 30)
    print("Доступные операции:")
    print("  + : Сложение")
    print("  - : Вычитание")
    print("  * : Умножение")
    print("  / : Деление")
    print("  % : Остаток от деления")
    print("  ^ : Возведение в степень")
    print("  q : Выход")
    print("-" * 30)
    
    while True:
        num1 = input("\nВведите первое число (или 'q' для выхода): ")
        if num1.lower() == 'q':
            print("До свидания!")
            break
            
        num1 = float(num1)
            
        operation = input("Введите операцию (+, -, *, /, %, ^): ")
        if operation.lower() == 'q':
            print("До свидания!")
            break
            
        num2 = input("Введите второе число: ")
        if num2.lower() == 'q':
            print("До свидания!")
            break
            
            
# Запуск калькулятора
if __name__ == "__main__":
    calc()