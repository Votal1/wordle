messages = {
    'uk': {
        'start': '👋 Ласкаво просимо до бота Wordle!\n\n'
                 '🍿 Готуйтесь до захоплюючої гри! Цей бот допоможе вам розминати мозок та весело проводити час.\n\n'
                 '📚 Щоб розпочати, перегляньте правила (/rules) та список команд (/help) '
                 'і оберіть мову, якою будете грати.\n\n'
                 'Щоб почати гру, натисніть\n/wordle',
        'select_unavailable': 'Неможливо міняти налаштування під час гри\n\n/cancel',
        'new_game': 'Розпочато нову гру\nВведи слово з 5 літер',
        'daily_game': 'Розпочато щоденну гру\nВведи слово з 5 літер',
        'cancel': 'Гру скасовано',
        'daily_already_won': 'Ви сьогодні вже виграли щоденну гру',
        'word_unavailable': 'Слово недоступне',
        'settings': '🌐 Тут можна обрати рівень складності та мову',
        'language_selected': 'Вибрано українську мову',
        'difficulty_selected': ['Вибрано легкий рівень складності',
                                'Вибрано нормальний рівень складності',
                                'Вибрано важкий рівень складності'],
        'top': ['Недостатньо інформації для створення рейтингу.',
                'Рейтинг кращих щоденних ігор за сьогодні',
                'Рейтинг гравців за щоденними перемогами',
                'Рейтинг гравців за перемогами'],
        'game_result': ['Ви програли.\nПравильне слово', 'Ви виграли!', 'Щоб зіграти знову, натисніть\n/wordle'],
        'stats': ['🏆 Кількість перемог: ', '🌞 Успішні щоденні ігри: ', '\n\nСьогоднішня щоденна гра:\n📊 Вгадування: ',
                  '\n🕰 Витрачено часу: ', 'більше години'],
        'rules': '📚 Правила гри\n\n'
                 '⛳ Ваше завдання — вгадати таємне слово.\n'
                 'Щоб почати — введіть будь-яке слово з п\'яти літер. '
                 'Усі ваші припущення мають бути справжніми словами зі словника. '
                 'Ви не можете придумати неіснуюче слово, як-от ЛДЕНР, просто щоб вгадати ці літери.\n\n'
                 '✍ Щойно ви введете слово — гра зафарбує кожну літеру кольором, щоб визначити, наскільки '
                 'слово близьке до прихованого.\n\n'
                 '⬜ Сірий квадрат означає, що ця буква взагалі не фігурує в секретному слові\n\n'
                 '🟨 Жовтий квадрат означає, що ця літера з\'являється в секретному слові, але вона '
                 'знаходиться не в тому місці слова\n\n'
                 '🟩 Зелений квадрат означає, що ця буква є в секретному слові, і вона знаходиться '
                 'саме в потрібному місці\n\n'
                 '🎉 Отримавши зелений або жовтий квадрат, ви наблизитесь до вгадування справжнього секретного '
                 'слова, оскільки це означає, що ви вгадали правильну букву.\n\n'
                 '🤝 CoWordle - схоже на Wordle, але на двох гравців, які відгадують слова по черзі. '
                 'Щоб зіграти, введи тег бота (@wordle1bot) в будь-якому чаті.\n\n'
                 '🌞 Грайте щоденні ігри (/daily), щоб зайняти місце в рейтингу кращих ігор за сьогодні та отримати '
                 '🧂 1-3, якщо ви зареєстровані у @RandomUA3bot',
        'links': '🇺🇦 @RandomUA3bot - гра в русаків та інші розваги\n'
                 '🇺🇦 @randomuanews - новини, патчноути, опитування\n'
                 '👨‍💻 <a href="https://t.me/vota_l">@vota_l</a> - завдяки ньому ти натиснув цю кнопку\n\n'
                 '💳 <a href="https://randomuabot.diaka.ua/donate?amount=30">Донат</a> - '
                 'задонать і отримай бонус в RandomUA3bot',
        'help': '/start - показати привітальне повідомлення\n'
                '/wordle - почати гру\n'
                '/daily - почати щоденну гру\n'
                '/help - список команд\n'
                '/me - ваша статистика\n'
                '/top - рейтинг, напиши "-d" або "-w" щоб побачити більше\n'
                '/rules - все, що вам треба знати\n'
                '/cancel - скасувати гру\n'
                '/links - донат та інші боти\n'
                '/settings - складність і мова\n'
                '@wordle1bot - зіграти в CoWordle',
        'inline': ['🤝 Зіграємо CoWordle?', 'Запрошую', 'можеш ввести @username', 'Так!', 'Складність: ',
                   'легко', 'нормально', 'важко'],
        'new_duel': '🤝 Почалась гра CoWordle.\nВаш суперник - ',
        'opponents_turn': 'Зараз хід суперника. Щоб скасувати гру, натисніть\n/cancel',
        'duel_started_call': '🤝  Почалась гра CoWordle',
        'cant_start': 'Почніть діалог з ботом',
        'cant_start_1': 'Ви вже у грі\nЩоб скасувати гру, натисніть\n/cancel',
        'cant_start_2': 'Ваш суперник вже у грі',
        'wrong_invite': 'Запрошення не для вас',
        'invite_expired': 'Запрошення прострочене',
        'own_invite': 'Ви не можете прийняти свій виклик'
    },

    'en': {
        'start': '👋 Welcome to the Wordle Bot!\n\n'
                 '🍿 Get ready for an exciting game! This bot will help you exercise your brain and have a great time.'
                 '\n\n📚 To begin, familiarize yourself with the rules (/rules) and list of commands (/help) and'
                 ' choose your language.\n\n'
                 'Start a new game by typing\n/wordle',
        'select_unavailable': 'It\'s not possible to change the settings during the game\n\n/cancel',
        'new_game': 'A new game has started\nEnter a 5-letter word',
        'daily_game': 'The daily game has started\nEnter a 5-letter word',
        'cancel': 'The game is cancelled',
        'daily_already_won': 'You have already won the daily game today',
        'word_unavailable': 'The word is incorrect',
        'settings': '🌐 Here you can choose the difficulty level and language',
        'language_selected': 'English is selected',
        'difficulty_selected': ['Easy difficulty selected',
                                'Normal difficulty selected',
                                'Hard difficulty selected'],
        'top': ['Insufficient information to create a rating.',
                'Today\'s best daily games rating',
                'Player rating by daily wins',
                'Player rating by wins'],
        'game_result': ['You lost.\nThe correct word is', 'You won!', 'Press /wordle to play again'],
        'stats': ['🏆 Wins: ', '🌞 Daily wins: ', '\n\nToday\'s daily game:\n📊 Guesses: ',
                  '\n🕰 Time used: ', 'more than an hour'],
        'rules': '📚 Rules\n\n'
                 '⛳ Your objective is to guess a secret word.\n'
                 'To submit a guess, type any five-letter word. '
                 'All of your guesses must be real words from dictionary. '
                 'You can\'t make up a non-existent word, like LDENR, just to guess those letters.\n\n'
                 '✍ As soon as you\'ve submitted your guess, the game will color-code each letter in your '
                 'guess to tell you how close it was to the letters in the hidden word.\n\n'
                 '⬜ A gray square means that this letter does not appear in the secret word at all\n\n'
                 '🟨 A yellow square means that this letter appears in the secret word, but it\'s in the wrong '
                 'spot within the word\n\n'
                 '🟩 A green square means that this letter appears in the secret word, and it\'s in exactly the '
                 'right place\n\n'
                 '🎉 Getting a green square or yellow square will get you closer to guessing the real secret word,'
                 ' since it means you\'ve guessed a correct letter.\n\n'
                 '🤝 CoWordle - similar to Wordle, but with two players who guess words in turn. '
                 'To play, enter the bot\'s username (@wordle1bot) in any chat\n\n'
                 '🌞 Play daily games (/daily) to rank in today\'s best games and get '
                 '🧂 1-3 if you are registered in @RandomUA3bot',
        'links': '🇺🇦 @RandomUA3bot - rusak game and other entertainments\n'
                 '🇺🇦 @randomuanews - news, patch notes, polls\n'
                 '👨‍💻 <a href="https://t.me/vota_l">@vota_l</a> - thanks to him you clicked this button\n\n'
                 '💳 <a href="https://randomuabot.diaka.ua/donate?amount=30">Donate</a> - '
                 'donate and get a bonus in RandomUA3bot',
        'help': '/start - show welcome message\n'
                '/wordle - start game\n'
                '/daily - start daily game\n'
                '/help - list of commands\n'
                '/me - your statistics\n'
                '/top - rating, add "-d" or "-w" to see more\n'
                '/rules - everything you need to know\n'
                '/cancel - finish game\n'
                '/links - donate and other bots\n'
                '/settings - difficulty and language\n'
                '@wordle1bot - play in CoWordle',
        'inline': ['🤝 Let\'s play CoWordle', 'I invite', 'you can enter @username', 'Yes!', 'Difficulty: ',
                   'easy', 'normal', 'hard'],
        'new_duel': '🤝 The CoWordle game has started\nYour opponent - ',
        'opponents_turn': 'Now it\'s your opponent\'s turn. To cancel the game, press\n/cancel',
        'duel_started_call': '🤝 The CoWordle game has started.',
        'cant_start': 'Start dialog with bot',
        'cant_start_1': 'You are already in the game\nPress /cancel to quit',
        'cant_start_2': 'Your opponent are already in the game',
        'wrong_invite': 'The invitation is not for you',
        'invite_expired': 'Invite expired',
        'own_invite': 'You cannot accept your invitation'
    }
}
