

#Функция выдаёт список городов из первого множества,
#за исключением тех, что уже были использованы во втором множестве

def print_valid_cities(all_cities, used_cities):
    cities = all_cities.difference(used_cities)
    for city in cities:
        print(city)
    # Вместо этого многоточия напишите код функции, она должна
    # принимать и обрабатывать аргументы all_cities и used_cities,
    # а затем печатать результат в нужном формате

all_cities = {
    'Абакан',
    'Астрахань', 
    'Бобруйск', 
    'Калуга',
    'Караганда',
    'Кострома',
    'Липецк', 
    'Новосибирск'
}

used_cities = {'Калуга', 'Абакан' , 'Новосибирск'}


print_valid_cities(all_cities, used_cities)