BASE_COST = 12000

DETAIL_COEFFICIENTS = {
    "Капот": 1,
    "Передняя дверь": 1.2,
    "Задняя дверь": 1.1,
    "Передний бампер": 1,
    "Задний бампер": 1,
    "Крыша": 1.1
}

def calculate_part_cost(part_name):
    if part_name in DETAIL_COEFFICIENTS:
        return BASE_COST * DETAIL_COEFFICIENTS[part_name]
    else:
        print("Ошибка: неизвестная деталь.")
        return 0

def get_part_input():
    part_name = input("Введите наименование детали (Капот, Передняя дверь, Задняя дверь, Передний бампер, Задний бампер, Крыша): ")
    return part_name
