import csv

def load_csv(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)

def parse_customer_data(row):
    return {
        "full_name": row["name"],
        "gender": row["sex"],
        "age": row["age"],
        "purchase_amount": row["bill"],
        "device": row["device_type"],
        "browser": row["browser"],
        "region": row["region"]
    }

def format_description(customer):
    gender_description = 'женского' if customer['gender'] == 'female' else 'мужского'
    return (f"Пользователь {customer['full_name']} "
            f"{gender_description} пола, {customer['age']} лет "
            f"совершила покупку на {customer['purchase_amount']} у.е. "
            f"с {customer['device']} браузера {customer['browser']}. "
            f"Регион из которого совершалась покупка: {customer['region']}.")

def write_descriptions_to_txt(descriptions, output_file):
    with open(output_file, mode='w', encoding='utf-8') as file:
        for description in descriptions:
            file.write(description + '\n')

def process_customers(input_csv, output_txt):
    customer_data = load_csv(input_csv)
    descriptions = [format_description(parse_customer_data(row)) for row in customer_data]
    write_descriptions_to_txt(descriptions, output_txt)

if __name__ == "__main__":
    input_csv_file = 'web_clients_correct.csv'
    output_txt_file = 'descriptions.txt'
    process_customers(input_csv_file, output_txt_file)
