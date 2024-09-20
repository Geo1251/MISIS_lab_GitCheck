from dev2 import calculate_part_cost, get_part_input

COLOR_COEFFICIENTS = {
    "Белый": 1,
    "Синий": 1,
    "Желтый": 1.1,
    "Красный": 1,
    "Перламутровый": 1.2,
    "Серый металлик": 1.3
}

def test_func():
    

def calculate_total_cost(part_name, color_name):
    part_cost = calculate_part_cost(part_name)
    color_coefficient = COLOR_COEFFICIENTS.get(color_name, None)
    
    if color_coefficient is not None:
        total_cost = part_cost * color_coefficient
        return total_cost
    else:
        print("Ошибка: неизвестный цвет.")
        return 0

def get_color_input():
    color_name = input("Введите цвет (Белый, Синий, Желтый, Красный, Перламутровый, Серый металлик): ")
    return color_name

if __name__ == "__main__":
    part_name = get_part_input()
    color_name = get_color_input()
    
    total_cost = calculate_total_cost(part_name, color_name)
    
    print(f"Итоговая стоимость покраски {part_name} в цвет {color_name}: {total_cost} рублей")
