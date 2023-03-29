def task_30():
    first_elem = int(input('Введите первый элемент:\t'))
    div = int(input('Введите разность:\t'))
    count = int(input('Введите количество:\t'))
    for i in range(count):
        print(first_elem + i * div)
