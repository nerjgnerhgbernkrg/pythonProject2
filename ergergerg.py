answers = {
    'git': 'Введи запрос для поиска в формате "GIT Запрос Язык_Программирования" и я дам тебе ссылки на 5 случайных репозиториев',
    'help': 'Я умею искать по гитхабу и повторять слова за тобой. Чтобы узнать, как искать, напиши мне слово git',
}


@bot.message_handler(commands=['start', 'help', 'get_city'])