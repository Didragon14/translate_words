# -*- coding: utf-8 -*-


def translate():

    # Иструкция
    help_message = """
    s - Поиск
    а - Добавить новое слово
    r - Удалить слово
    k - Показать все слова
    d - Показать весь словарь
    h - Справка
    q - Выход
    """

    # Перевод слова english to russian
    translate_dict = {
    'apple': 'яблоко',
    'bold': 'жирный',
    'bus': 'автобус',
    'cat': 'кошка',
    'car': 'машина'
    }

    print("=" * 15, "Translate v0.1", "=" * 15)

    
    choise = ''

    while choise != 'q':
        choise = input('\n(h)>> ')
        
        if choise == 'h':       # Иструкция
            print(help_message)        
        
        elif choise == 's':     # Поиск слов
            word = input('Введите для поиска английских слов: ')
            res = translate_dict.get(word, 'Не найдено!')
            print(res)
        
        elif choise == 'a':     # Добавления в слов в словарь
            word_key = input('Введите английское слово: ')
            word_value = input('Введите слово перевода на русском: ')
            translate_dict[word_key] = word_value
            print('Слово добавлено!')
        
        elif choise == 'r':     # Удаления слов из словаря
            word = input('Введите английское слово, которое хотите удалить: ')
            print(translate_dict.pop(word, 'Не найдено!'))
        
        elif choise == 'k':     # Вывод каждого englis слова
            for i in translate_dict:
                print(i, end=' ')
        
        elif choise == 'd':     # Вывод каждого english and russian слова
            for i in translate_dict:
                print(f'{i} - {translate_dict[i]};', end=' ')
        
        elif choise == 'q':     # Выход
            print('До свидания!')
            break
        
        else:
            print('Почитайте инструкцию в (h)')

translate()