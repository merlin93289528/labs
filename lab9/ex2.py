base = {
    'Суп' : {
        'count_el' : 2,
        'elements' : ['картошка', 'вода'],
        'time' : 10
    },
    'Салат' : {
        'count_el' : 2,
        'elements' : ['помідор', 'огірок'],
        'time' : 5
    },
    'Стейк' : {
        'count_el' : 1,
        'elements' : ['мясо'],
        'time' : 20
    }
}

while True:
    task = input('Виберіть дію:\n1. Записати рецепт\n2. Знайти рецепт за максимальним часом\n')
    if task == '1':

        label = input('Введіть назву блюда: ')
        base[label] = {}
        base[label]['count_el'] = int(input('Введіть кількість інгрідієнтів блюда: '))
        base[label]['elements'] = input('Введіть інгрідіенти через пробіл: ').split(' ')
        base[label]['time'] = int(input('Введіть час готовки: '))

    elif task == '2':

        maxtime = int(input('Введіть максимальний час приготування: '))

        result = []
        for food in base:
            if base[food]['time'] <= maxtime:
                result.append(food)

        print(result)
