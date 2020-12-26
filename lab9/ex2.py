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

task = int(input('Введіть максимальний час за який має готуватись страва: '))
result = []
for food in base:
    if base[food]['time'] <= task:
        result.append(food)

print(result)