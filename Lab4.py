import json
import xml.etree.ElementTree as ET

# Чтение данных из файла JSON
with open('data.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# Создание корневого элемента XML
root = ET.Element("Люди")

# Конвертация каждого элемента из JSON в XML
for person in data:
    person_element = ET.SubElement(root, 'Человек')

    for key, value in person.items():
        child = ET.SubElement(person_element, key)
        child.text = str(value)

# Запись данных в файл XML
tree = ET.ElementTree(root)
with open('data.xml', 'wb') as xml_file:
    tree.write(xml_file, encoding='utf-8', xml_declaration=True)

print("Конвертация завершена. Данные записаны в data.xml.")