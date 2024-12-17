import re
def validate_car_id(car_id):
    pattern = r'^[А-Я]{1}\d{3}[А-Я]{2}\d{2,3}$'

    match = re.match(pattern, car_id)

    if match:
        number = car_id[:-2]
        region = car_id[-2:]
        return f"Номер {number} валиден. Регион: {region}."
    else:
        return "Номер не валиден."

car_id1 = 'А222BС96'
result1 = validate_car_id(car_id1)
print(result1)

car_id2 = 'А22ВВ193'
result2 = validate_car_id(car_id2)
print(result2) 
