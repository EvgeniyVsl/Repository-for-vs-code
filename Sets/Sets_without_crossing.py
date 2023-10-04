def get_together_games(game_3, game_2):
    together_games= set(game_3).intersection(set(game_2))# Напишите здесь код функции для поиска пересечений
    for game in together_games:
        print('👾',game)
anfisa_games = [
    'Online-chess',
    'Города',
    'DOOM',
    'Крестики-нолики',
    'GTA'
]
alisa_games = [
    'DOOM',
    'Online-chess',
    'Города',
    'GTA',
    'World of tanks'
]
# Вызовите функцию со списками игр в качестве параметров
get_together_games(anfisa_games, alisa_games)

