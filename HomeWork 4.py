def move_disk(disk, source_peg, destination):
    print(f'Блин {disk}: Стержень {source_peg} -> Стержень {destination}.')
    with open('решение.txt', 'a') as file:
        file.write(f'Блин {disk}: Стержень {source_peg} -> Стержень {destination}.\n')
def TowerofHanoi(n, source_peg, destination, auxiliary_peg):
    if n==1:
        move_disk(1, source_peg, destination)
    else:
        TowerofHanoi(n-1, source_peg, auxiliary_peg, destination)
        move_disk(n, source_peg, destination)
        TowerofHanoi(n-1, auxiliary_peg, destination, source_peg)
def main():
    try:
        num_disks = int(input("Введите количество дисков: "))
        if num_disks<1:
            raise ValueError("Количество дисков должно быть >0.")
        with open('решение.txt', 'w') as file:
            file.write(f'Решение задачи Ханойской башни для {num_disks} дисков:\n')
        TowerofHanoi(num_disks,1,3,2)
    except ValueError as e:
        print(f'Ошибка ввода: {e}')
if __name__ == "__main__":
    main()