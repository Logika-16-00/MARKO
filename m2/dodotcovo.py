def вивести_вміст_файлу(filename):
    try:
        with open(filename, 'r') as file:
            вміст = file.read()
            print(вміст)
    except FileNotFoundError:
        print("Файл не знайдений")

def додати_запис(filename):
    запис = input("Введіть новий запис: ")
    with open(filename, 'a') as file:
        file.write(запис + "\n")

def пошук_ключового_слова(filename):
    ключове_слово = input("Введіть ключове слов: ")
    try:
        with open(filename, 'r') as file:
            for line in file:
                if ключове_слово.lower() in line.lower():
                    print(line.strip())
    except FileNotFoundError:
        print("Файл не знайдений")

def головна_функція():
    filename = "file.txt"
    вивести_вміст_файлу(filename)

    while True:
        команда = input("Введіть команду (вийти, додати, друкувати, пошук): ")
        if команда == "вийти":
            break
        elif команда == "додати":
            додати_запис(filename)
        elif команда == "друкувати":
            вивести_вміст_файлу(filename)
        elif команда == "пошук":
            пошук_ключового_слова(filename)
        else:
            print("Невідома команда")

головна_функція()