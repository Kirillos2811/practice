from datetime import datetime


print("Введите последовательно дату вашего рождения")
print("День")
day = int(input())

print("Месяц")
month = int(input())

print("Год")
year = int(input())

date = datetime(year, month, day)
now = datetime.now()

def weekday():
    print("Этот день был ", end='')

    match date.isoweekday():
        case 1:
            print("понедельником")
        case 2:
            print("вторником")
        case 3:
            print("средой")
        case 4:
            print("четвергом")
        case 5:
            print("пятницей")
        case 6:
            print("субботой")
        case 7:
            print("воскресеньем")


def year_type():
    try:
        datetime(year, 2, 29)
        print("Это был високосный год")
    except ValueError:
        print("Это был не високосный год")

def age():
    if now < datetime(now.year, month, day):
        print("Вам сейчас",now.year - date.year - 1,"лет")
    else:
        print("Вам сейчас",now.year - date.year,"лет")


def print_date():
    date_to_print = str(date.day) + str(date.month) + str(date.year)
    symbols = {
        '0': ['***', '* *', '* *', '* *', '***'],
        '1': ['  *', '  *', '  *', '  *', '  *'],
        '2': ['***', '  *', '***', '*  ', '***'],
        '3': ['***', '  *', '***', '  *', '***'],
        '4': ['* *', '* *', '***', '  *', '  *'],
        '5': ['***', '*  ', '***', '  *', '***'],
        '6': ['***', '*  ', '***', '* *', '***'],
        '7': ['***', '  *', '  *', '  *', '  *'],
        '8': ['***', '* *', '***', '* *', '***'],
        '9': ['***', '* *', '***', '  *', '***'],
        '.': [' ', ' ', ' * ', '   ', ' ']
    }


    lines = ['', '', '', '', '']


    for char in date_to_print:
        part_of_symbol = symbols.get(char, [' ', ' ', ' ', ' ', ' '])
        for i in range(5):
            lines[i] += part_of_symbol[i] + '  '


    for line in lines:
        print(line)


weekday()
year_type()
age()
print_date()