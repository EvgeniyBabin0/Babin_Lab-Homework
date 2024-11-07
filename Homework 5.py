from datetime import datetime
def parse_date(date_string):
    """Пытается распарсить строку даты в объект datetime."""
    formats = [
        "%A, %B %d, %Y",  # The Moscow Times — Wednesday, October 2, 2002
        "%A, %d.%m.%y",  # The Guardian — Friday, 11.10.13
        "%A, %d %B %Y"  # Daily News — Thursday, 18 August 1977
    ]

    for fmt in formats:
        try:
            return datetime.strptime(date_string, fmt)
        except ValueError:
            continue

    raise ValueError("Дата не соответствует ни одному из форматов.")
def main():
    print("Введите дату в одном из следующих форматов:")
    print("1. 'Wednesday, October 2, 2002'")
    print("2. 'Friday, 11.10.13'")
    print("3. 'Thursday, 18 August 1977'")
    print("Для выхода введите 'exit'.")

    while True:
        user_input=input("Введите дату: ")

        if user_input.lower()=='exit':
            break
        try:
            date_object=parse_date(user_input)
            print(f"Объект datetime: {date_object}")
        except ValueError as e:
            print(e)
if __name__ == "__main__":
    main()