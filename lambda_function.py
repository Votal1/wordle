import json
import os
import boto3
import telebot
import redis
from datetime import datetime
from random import randint
from PIL import Image, ImageDraw, ImageFont
from botocore.exceptions import ClientError
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, InlineQueryResultArticle, InputTextMessageContent
from modules.locales import messages
from modules.top import top_today, top_daily, top_wins

bot = telebot.TeleBot(os.environ.get('TOKEN'))
r = redis.Redis(host=os.environ.get('REDIS_HOST'), port=int(os.environ.get('REDIS_PORT')),
                password=os.environ.get('REDIS_PASSWORD'), db=0)


def fill_square(text, solution, column, keyboard):
    letters = {}
    stats = ''
    for letter in solution:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1

    i = 0
    for letter in text:
        if letter == solution[i]:
            letters[letter] -= 1
        i += 1

    i = 0
    line = text[:column]
    for letter in line:
        if letter in solution and letter != solution[i] and letter in line:
            letters[letter] -= 1
            line = line.replace(letter, '', 1)
        i += 1

    green = (76, 175, 80)
    yellow = (255, 235, 59)
    gray = (165, 174, 196)
    if text[column] == solution[column]:
        fill_color = outline_color = green
        keyboard[text[column]] = green
        stats += '🟩'
    elif text[column] in solution and text[column] in letters and letters[text[column]] > 0:
        fill_color = outline_color = yellow
        stats += '🟨'
        if text[column] not in keyboard or keyboard[text[column]] != green:
            keyboard[text[column]] = yellow
    else:
        fill_color = outline_color = gray
        stats += '⬛'
        if text[column] not in keyboard or keyboard[text[column]] not in (green, yellow):
            keyboard[text[column]] = gray
    return fill_color, outline_color, keyboard, stats


def generate(text0, text1, text2, text3, text4, text5, textx, files, language):
    stats = line = ''
    keyboard = {}

    square_size = 100
    gap_size = 20
    width = square_size * 5 + gap_size * 6
    height = square_size * 6 + gap_size * 7

    image = Image.new("RGBA", (width, height), color=(0, 0, 0, 0))

    draw = ImageDraw.Draw(image)
    for row in range(6):
        stats += '\n'
        for col in range(5):
            x0 = col * square_size + (col + 1) * gap_size
            y0 = row * square_size + (row + 1) * gap_size
            x1 = x0 + square_size
            y1 = y0 + square_size
            fill_color = (251, 252, 255)
            outline_color = (222, 225, 233)
            radius = 10  # radius of the rounded corners
            draw.rounded_rectangle((x0, y0, x1, y1), radius=radius, fill=fill_color, outline=outline_color, width=2)
            if row == 0 and text0:
                fill_color, outline_color, keyboard, line = fill_square(text0, textx, col, keyboard)
                if fill_color:
                    draw.rounded_rectangle((x0, y0, x1, y1), radius=radius, fill=fill_color, outline=outline_color)
                font = ImageFont.truetype("arial.ttf", 60)
                text = text0[col]
                text_length = draw.textlength(text, font=font)
                text_x = x0 + (square_size - text_length) // 2
                text_y = y0 + (square_size - font.size) // 2
                draw.text((text_x, text_y), text, font=font, fill=(0, 0, 0), stroke_width=1, stroke_fill=(0, 0, 0))
            elif row == 1 and text1:
                fill_color, outline_color, keyboard, line = fill_square(text1, textx, col, keyboard)
                if fill_color:
                    draw.rounded_rectangle((x0, y0, x1, y1), radius=radius, fill=fill_color, outline=outline_color)
                font = ImageFont.truetype("arial.ttf", 60)
                text = text1[col]
                text_length = draw.textlength(text, font=font)
                text_x = x0 + (square_size - text_length) // 2
                text_y = y0 + (square_size - font.size) // 2
                draw.text((text_x, text_y), text, font=font, fill=(0, 0, 0), stroke_width=1, stroke_fill=(0, 0, 0))
            elif row == 2 and text2:
                fill_color, outline_color, keyboard, line = fill_square(text2, textx, col, keyboard)
                if fill_color:
                    draw.rounded_rectangle((x0, y0, x1, y1), radius=radius, fill=fill_color, outline=outline_color)
                font = ImageFont.truetype("arial.ttf", 60)
                text = text2[col]
                text_length = draw.textlength(text, font=font)
                text_x = x0 + (square_size - text_length) // 2
                text_y = y0 + (square_size - font.size) // 2
                draw.text((text_x, text_y), text, font=font, fill=(0, 0, 0), stroke_width=1, stroke_fill=(0, 0, 0))
            elif row == 3 and text3:
                fill_color, outline_color, keyboard, line = fill_square(text3, textx, col, keyboard)
                if fill_color:
                    draw.rounded_rectangle((x0, y0, x1, y1), radius=radius, fill=fill_color, outline=outline_color)
                font = ImageFont.truetype("arial.ttf", 60)
                text = text3[col]
                text_length = draw.textlength(text, font=font)
                text_x = x0 + (square_size - text_length) // 2
                text_y = y0 + (square_size - font.size) // 2
                draw.text((text_x, text_y), text, font=font, fill=(0, 0, 0), stroke_width=1, stroke_fill=(0, 0, 0))
            elif row == 4 and text4:
                fill_color, outline_color, keyboard, line = fill_square(text4, textx, col, keyboard)
                if fill_color:
                    draw.rounded_rectangle((x0, y0, x1, y1), radius=radius, fill=fill_color, outline=outline_color)
                font = ImageFont.truetype("arial.ttf", 60)
                text = text4[col]
                text_length = draw.textlength(text, font=font)
                text_x = x0 + (square_size - text_length) // 2
                text_y = y0 + (square_size - font.size) // 2
                draw.text((text_x, text_y), text, font=font, fill=(0, 0, 0), stroke_width=1, stroke_fill=(0, 0, 0))
            elif row == 5 and text5:
                fill_color, outline_color, keyboard, line = fill_square(text5, textx, col, keyboard)
                if fill_color:
                    draw.rounded_rectangle((x0, y0, x1, y1), radius=radius, fill=fill_color, outline=outline_color)
                font = ImageFont.truetype("arial.ttf", 60)
                text = text5[col]
                text_length = draw.textlength(text, font=font)
                text_x = x0 + (square_size - text_length) // 2
                text_y = y0 + (square_size - font.size) // 2
                draw.text((text_x, text_y), text, font=font, fill=(0, 0, 0), stroke_width=1, stroke_fill=(0, 0, 0))
            stats += line

    image.save(f'/tmp/{files[0]}', "WEBP")

    square_size = 100
    gap_size = 20
    width = square_size * 11 + gap_size * 12
    height = square_size * 3 + gap_size * 4 + 150

    image = Image.new("RGBA", (width, height), color=(0, 0, 0, 0))

    key_color = (251, 252, 255)
    key_outline_color = (222, 225, 233)
    radius = 10
    font = ImageFont.truetype("arial.ttf", 80)

    # Define the characters for each key
    keys = [
        'ЙЦУКЕНГШЩЗХ',
        'ФІВАПРОЛДЖЄ',
        'ҐЯЧСМИТЬБЮЇ'
    ]
    if language.startswith('words-en'):
        keys = [
            'QWERTYUIOP',
            'ASDFGHJKL',
            'ZXCVBNM'
        ]

    draw = ImageDraw.Draw(image)

    for row in range(len(keys)):
        for col in range(len(keys[row])):
            x0 = col * square_size + (col + 1) * gap_size
            if row == 1 and language.startswith('words-en'):
                x0 = col * square_size + (col + 4) * gap_size
            if row == 2 and language.startswith('words-en'):
                x0 = col * square_size + (col + 10) * gap_size
            y0 = row * square_size + (row + 1) * gap_size
            x1 = x0 + square_size
            y1 = y0 + square_size
            fill_color = key_color
            outline_color = key_outline_color
            char = keys[row][col]
            if char != ' ':
                if char in keyboard:
                    fill_color = outline_color = keyboard[char]
                draw.rounded_rectangle((x0, y0, x1, y1), radius=radius, fill=fill_color, outline=outline_color, width=2)
                char_length = font.getlength(char)
                char_x = x0 + (square_size - char_length) // 2
                char_y = y0 + (square_size - font.size) // 2
                draw.text((char_x, char_y), char, font=font, fill=(0, 0, 0))

    image.save(f'/tmp/{files[1]}', "WEBP")

    while stats.strip().endswith('🟩🟩🟩🟩🟩\n🟩🟩🟩🟩🟩'):
        stats = stats.strip()[:-5].strip()

    return stats


def get_words(uid):
    w0 = r.hget(uid, 'word0').decode().upper()
    w1 = r.hget(uid, 'word1').decode().upper()
    w2 = r.hget(uid, 'word2').decode().upper()
    w3 = r.hget(uid, 'word3').decode().upper()
    w4 = r.hget(uid, 'word4').decode().upper()
    w5 = r.hget(uid, 'word5').decode().upper()
    solution = r.hget(uid, 'solution').decode().upper()
    language = r.hget(uid, 'language_code').decode()
    return w0, w1, w2, w3, w4, w5, solution, language


def get_secret():
    secret_name = "prod/redis/randombot"
    region_name = "eu-central-1"

    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        raise e

    return json.loads(get_secret_value_response['SecretString'])


def complete_daily(uid):
    secrets = get_secret()
    r2 = redis.Redis(
        host=secrets['HOST'],
        port=int(secrets['PORT']),
        username=secrets['USERNAME'],
        password=secrets['PASSWORD'],
        db=0
    )

    salt = randint(1, 3)

    if r2.hexists(uid, 'name'):

        if int(r2.hget(uid, 'weapon')) == 10:
            salt = 3
            r2.hincrby(uid, 's_weapon', -1)
            if int(r2.hget(uid, 's_weapon')) <= 0:
                if int(r2.hget(uid, 'class')) in (6, 16, 26):
                    r2.hset(uid, 'weapon', 16)
                else:
                    r2.hset(uid, 'weapon', 0)

        r2.hincrby(uid, 'salt', salt)
        r2.hincrby(uid, 'wordle_wins', 1)
        r2.hset(uid, 'wordle_time', datetime.now().day)
        return salt
    return 0


def choose_lang(uid, settings=False):
    markup = InlineKeyboardMarkup()
    if settings:
        colors = ['🟢', '🔵', '🔴']
        dictionary = r.hget(uid, 'dictionary').decode()
        if dictionary.endswith('ua') or dictionary.endswith('en'):
            colors[0] = '➡🟢'
        elif dictionary.endswith('all'):
            colors[2] = '➡🔴'
        else:
            colors[1] = '➡🔵'
        markup.add(InlineKeyboardButton(text=colors[0], callback_data='choose_difficulty_easy'),
                   InlineKeyboardButton(text=colors[1], callback_data='choose_difficulty_normal'),
                   InlineKeyboardButton(text=colors[2], callback_data='choose_difficulty_hard'))
    flags = ['🇬🇧', '🇺🇦']
    if r.hget(uid, 'language_code').decode().endswith('uk'):
        flags[1] = '➡🇺🇦'
    else:
        flags[0] = '➡🇬🇧'
    markup.add(InlineKeyboardButton(text=flags[0], callback_data='choose_lang_en'),
               InlineKeyboardButton(text=flags[1], callback_data='choose_lang_uk'))
    return markup


def get_message(uid, key, language_code=''):
    if not language_code:
        if r.hexists(uid, 'language_code'):
            language_code = r.hget(uid, 'language_code').decode()
        else:
            language_code = 'en'

    return messages.get(language_code, 'en').get(key)


def callback(body):
    uid = body['callback_query'].get('from').get('id')
    cdata = body['callback_query'].get('data')
    call_id = body['callback_query'].get('id')
    firstname = body['callback_query'].get('from').get('first_name')
    if cdata.startswith('choose_'):
        cid = body['callback_query'].get('message').get('chat').get('id')
        text = body['callback_query'].get('message').get('text')
        mid = body['callback_query'].get('message').get('message_id')
        if not r.hexists(uid, 'game') or r.hget(uid, 'game').decode() == 'none':
            answer = ''
            if cdata.startswith('choose_lang_en'):
                r.hset(uid, 'language_code', 'en', {
                    'dictionary': 'words-en',
                    'whole_dictionary': 'words-en-all'
                })
                answer = get_message(uid, 'language_selected', language_code='en')
            elif cdata.startswith('choose_lang_uk'):
                r.hset(uid, 'language_code', 'uk', {
                    'dictionary': 'words-ua',
                    'whole_dictionary': 'words-ua-all'
                })
                answer = get_message(uid, 'language_selected', language_code='uk')

            elif cdata.startswith('choose_difficulty_easy'):
                language_code = r.hget(uid, 'language_code').decode()
                if language_code == 'uk':
                    dictionary = ['words-ua', 'words-ua-all']
                else:
                    dictionary = ['words-en', 'words-en-all']
                r.hset(uid, 'dictionary', dictionary[0], {'whole_dictionary': dictionary[1]})
                answer = get_message(uid, 'difficulty_selected')[0]

            elif cdata.startswith('choose_difficulty_normal'):
                language_code = r.hget(uid, 'language_code').decode()
                if language_code == 'uk':
                    dictionary = ['words-ua-nouns', 'words-ua-all']
                else:
                    dictionary = ['words-en-popular', 'words-en-all']
                r.hset(uid, 'dictionary', dictionary[0], {'whole_dictionary': dictionary[1]})
                answer = get_message(uid, 'difficulty_selected')[1]

            elif cdata.startswith('choose_difficulty_hard'):
                language_code = r.hget(uid, 'language_code').decode()
                if language_code == 'uk':
                    dictionary = ['words-ua-all', 'words-ua-all']
                else:
                    dictionary = ['words-en-all', 'words-en-all']
                r.hset(uid, 'dictionary', dictionary[0], {'whole_dictionary': dictionary[1]})
                answer = get_message(uid, 'difficulty_selected')[2]

            try:
                settings, key = False, 'start'
                if len(body['callback_query'].get('message').get('reply_markup').get('inline_keyboard')[0]) > 2:
                    settings, key = True, 'settings'
                msg = get_message(uid, key)
                bot.edit_message_text(text=msg, chat_id=cid, message_id=mid, reply_markup=choose_lang(uid, settings))
            except:
                pass
            bot.answer_callback_query(callback_query_id=call_id, show_alert=True, text=answer)
        else:
            msg = get_message(uid, 'select_unavailable')
            bot.answer_callback_query(callback_query_id=call_id, show_alert=True, text=msg)
    elif cdata.startswith('accept'):
        stats = cdata.split(',')
        uid2 = stats[1]
        print(body)
        if int(uid) != int(uid2):
            if int(stats[3]) == int(r.hget(uid2, 'active_duel')):
                username = True
                if str(stats[2]).startswith('@'):
                    if 'username' in body['callback_query'].get('from') \
                            and body['callback_query'].get('from').get('username') == stats[2][1:]:
                        username = True
                    else:
                        username = False
                if username:
                    if str(uid).encode() in r.smembers('everyone'):
                        if not r.hexists(uid, 'game') or r.hget(uid, 'game').decode() == 'none':
                            if not r.hexists(uid2, 'game') or r.hget(uid2, 'game').decode() == 'none':
                                bot.edit_message_reply_markup(
                                    inline_message_id=body['callback_query'].get('inline_message_id'),
                                    reply_markup=None
                                )
                                sol = r.srandmember(r.hget(uid2, 'dictionary'))
                                r.hset(uid, 'game', 'wordle', {
                                    'daily': 0,
                                    'word0': '',
                                    'word1': '',
                                    'word2': '',
                                    'word3': '',
                                    'word4': '',
                                    'word5': '',
                                    'solution': sol,
                                    'duel': uid2,
                                    'turn': uid,
                                    'duel_dict': r.hget(uid2, 'whole_dictionary')
                                })
                                r.hset(uid2, 'game', 'wordle', {
                                    'daily': 0,
                                    'word0': '',
                                    'word1': '',
                                    'word2': '',
                                    'word3': '',
                                    'word4': '',
                                    'word5': '',
                                    'solution': sol,
                                    'duel': uid,
                                    'turn': uid,
                                    'duel_dict': r.hget(uid2, 'whole_dictionary'),
                                    'active_duel': 0
                                })
                                msg = get_message(uid, 'new_game')
                                msg2 = get_message(uid, 'new_duel')
                                msg2 += firstname
                                bot.send_message(uid, msg)
                                bot.send_message(uid2, msg2)
                                bot.send_sticker(uid, open('img1.webp', "rb"))

                                msg3 = get_message(uid, 'duel_started_call')
                                bot.answer_callback_query(callback_query_id=call_id, show_alert=True, text=msg3)
                            else:
                                msg = get_message(uid, 'cant_start_2')
                                bot.answer_callback_query(callback_query_id=call_id, show_alert=True, text=msg)
                        else:
                            msg = get_message(uid, 'cant_start_1')
                            bot.answer_callback_query(callback_query_id=call_id, show_alert=True, text=msg)
                    else:
                        msg = get_message(uid, 'cant_start')
                        bot.answer_callback_query(callback_query_id=call_id, show_alert=True, text=msg)
                else:
                    msg = get_message(uid, 'wrong_invite')
                    bot.answer_callback_query(callback_query_id=call_id, show_alert=True, text=msg)
            else:
                msg = get_message(uid, 'invite_expired')
                bot.answer_callback_query(callback_query_id=call_id, show_alert=True, text=msg)
        else:
            msg = get_message(uid, 'own_invite')
            bot.answer_callback_query(callback_query_id=call_id, show_alert=True, text=msg)


def inline(body):
    print(body)
    uid = body['inline_query'].get('from').get('id')
    q_id = body['inline_query'].get('id')
    query = body['inline_query'].get('query')
    update_id = body['update_id']
    if query == '':
        query = '1'
    markup = InlineKeyboardMarkup()
    call = f'accept,{uid},{query},{update_id}'

    msg = get_message(uid, 'inline')

    description = msg[2]
    text = msg[0]
    if query.startswith('@'):
        text += f'\n{msg[1]} {query}'
    r.hset(uid, 'active_duel', update_id)

    lc = r.hget(uid, 'language_code').decode()
    dictionary = r.hget(uid, 'dictionary').decode()

    if lc == 'uk':
        text += '\n🇺🇦 '
    else:
        text += '\n🇬🇧 '
    if dictionary.endswith('ua') or dictionary.endswith('en'):
        text += f'{msg[4]}{msg[5]}'
    elif dictionary.endswith('all'):
        text += f'{msg[4]}{msg[7]}'
    else:
        text += f'{msg[4]}{msg[6]}'

    text += '\n\n@wordle1bot'
    reply = InlineQueryResultArticle(
        id='1',
        title='CoWordle',
        description=description,
        input_message_content=InputTextMessageContent(text, disable_web_page_preview=True),
        reply_markup=markup.add(InlineKeyboardButton(text=msg[3], callback_data=call)),
        thumbnail_url='https://i.ibb.co/qxFmHbH/photo-2023-05-20-17-51-18.jpg')
    bot.answer_inline_query(q_id, results=[reply], cache_time=0)


def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])

        if 'inline_query' in body:
            inline(body)

        if 'callback_query' in body:
            callback(body)

        text = body['message'].get('text')
        uid = body['message'].get('from').get('id')
        cid = body['message'].get('chat').get('id')
        ct = body['message'].get('chat').get('type')
        lc = body['message'].get('from').get('language_code')
        fn = body['message'].get('from').get('first_name')

        print(body)
        print(uid, cid, ct)
        if ct == 'private':
            if text.startswith('/start'):
                if lc not in ('uk', 'en'):
                    lc = 'en'
                if str(uid).encode() not in r.smembers('everyone'):
                    r.sadd('everyone', uid)
                    if lc == 'uk':
                        dictionary = 'ua'
                    else:
                        dictionary = lc
                    r.hset(uid, 'firstname', fn, {
                        'dictionary': f'words-{dictionary}',
                        'whole_dictionary': f'words-{dictionary}-all',
                        'language_code': lc,
                        'daily_time': 0
                    })
                msg = get_message(uid, 'start')
                bot.send_message(cid, msg, reply_markup=choose_lang(uid))

            if text.startswith('/settings'):
                msg = get_message(uid, 'settings')
                bot.send_message(cid, msg, reply_markup=choose_lang(uid, settings=True))

            elif text.startswith('/rules'):
                msg = get_message(uid, 'rules')
                bot.send_message(cid, msg)

            elif text.startswith('/help'):
                msg = get_message(uid, 'help')
                bot.send_message(cid, msg)

            elif text.startswith('/links'):
                msg = get_message(uid, 'links')
                bot.send_message(cid, msg, disable_web_page_preview=True, parse_mode='HTML')

            elif text.startswith('/me'):
                wins, wins_d = 0, 0
                stats = get_message(uid, 'stats')
                if r.hexists('wins', uid):
                    wins = int(r.hget('wins', uid))
                msg = f'📜 {fn}\n\n{stats[0]}{wins}'
                if r.hexists('daily', uid):
                    daily = json.loads(r.hget('daily', uid).decode())
                    wins_d = daily['daily_wins']
                    msg += f'\n{stats[1]}{wins_d}'
                    if int(r.hget(uid, 'daily_time')) == datetime.now().day:
                        if daily['time_used'] >= 3600:
                            t = stats[4]
                        else:
                            ts = datetime.fromtimestamp(daily['time_used'])
                            t = ts.strftime("%M:%S")
                        msg += f'{stats[2]}{daily["tries"]}{stats[3]}{t}'
                else:
                    msg += f'\n{stats[1]}0'
                bot.send_message(cid, msg, disable_web_page_preview=True)

            elif text.startswith('/top'):
                stats = get_message(uid, 'top')
                if text.startswith('/top -d'):
                    msg = top_daily(r.hgetall('daily'), stats[0], stats[2])
                elif text.startswith('/top -w'):
                    msg = top_wins(r.hgetall('wins'), r.hgetall('daily'), stats[0], stats[3])
                else:
                    msg = top_today(r.hgetall('daily'), stats[0], stats[2])
                bot.send_message(cid, msg, disable_web_page_preview=True)

            elif text.startswith('/wordle'):
                dictionary = r.hget(uid, 'dictionary').decode()
                r.hset(uid, 'game', 'wordle', {
                    'daily': 0,
                    'word0': '',
                    'word1': '',
                    'word2': '',
                    'word3': '',
                    'word4': '',
                    'word5': '',
                    'solution': r.srandmember(dictionary)
                })
                r.hdel(uid, 'duel')

                msg = get_message(uid, 'new_game')
                bot.send_message(cid, msg)
                bot.send_sticker(cid, open('img1.webp', "rb"))

            elif text.startswith('/daily'):
                if int(r.hget(uid, 'daily_time')) != datetime.now().day:
                    dictionary = r.hget(uid, 'dictionary').decode()
                    r.hset(uid, 'game', 'wordle', {
                        'daily': 1,
                        'word0': '',
                        'word1': '',
                        'word2': '',
                        'word3': '',
                        'word4': '',
                        'word5': '',
                        'solution': r.srandmember(dictionary)
                    })
                    r.hdel(uid, 'duel')

                    if not r.hexists(uid, 'daily_start'):
                        r.hset(uid, 'daily_start', int(datetime.now().timestamp()))

                    msg = get_message(uid, 'daily_game')
                    bot.send_message(cid, msg)
                    bot.send_sticker(cid, open('img1.webp', "rb"))
                else:
                    msg = get_message(uid, 'daily_already_won')
                    bot.send_message(cid, msg)

            elif text.startswith('/cancel'):
                r.hset(uid, 'game', 'none', {'daily': 0})
                r.hdel(uid, 'duel')
                msg = get_message(uid, 'cancel')
                bot.send_message(cid, msg)

            else:
                if r.hget(uid, 'game').decode() == 'wordle':
                    if len(text) == 5:
                        dictionary = r.hget(uid, 'whole_dictionary').decode()
                        your_turn, enemy = True, 0
                        if r.hexists(uid, 'duel'):
                            enemy = int(r.hget(uid, 'duel'))
                            if r.hexists(enemy, 'duel') and int(r.hget(enemy, 'duel')) == uid:
                                turn = int(r.hget(uid, 'turn'))
                                if turn != uid:
                                    your_turn = False
                                dictionary = r.hget(uid, 'duel_dict').decode()
                            else:
                                enemy = 0
                        if text.lower().encode() in r.smembers(dictionary):
                            if your_turn:
                                correct = r.hget(uid, 'solution').decode().upper()
                                text = text.upper()

                                msg = ''
                                try_n = 0
                                for n in range(6):
                                    if not len(r.hget(uid, f'word{n}').decode()):
                                        try_n = n + 1
                                        r.hset(uid, f'word{n}', text)
                                        if enemy:
                                            r.hset(uid, f'turn', enemy)
                                            r.hset(enemy, f'word{n}', text, {'turn': enemy})
                                        break
                                results = get_message(uid, 'game_result')
                                if len(r.hget(uid, 'word5').decode()) > 0 and text != correct:
                                    msg = f'{results[0]} - {correct}\n\n'
                                    if int(r.hget(uid, 'daily')) == 1 and not enemy:
                                        msg += '/daily'
                                    else:
                                        msg += '/wordle'
                                files = [f'words{uid}.webp', f'kb{uid}.webp']
                                w0, w1, w2, w3, w4, w5, solution, language = get_words(uid)
                                stats = generate(w0, w1, w2, w3, w4, w5, solution, files, dictionary)
                                bot.send_sticker(cid, open(f'/tmp/{files[0]}', "rb"))
                                if enemy:
                                    bot.send_sticker(enemy, open(f'/tmp/{files[0]}', "rb"))
                                if text == correct or msg:
                                    r.hset(uid, 'game', 'none')
                                    if enemy:
                                        r.hset(enemy, 'game', 'none')
                                    if text == correct:
                                        msg = f'<code>🏆 {results[1]}\n\n{stats}\n\n📩 @wordle1bot</code>' \
                                              f'\n\n'
                                        if int(r.hget(uid, 'daily')) == 1 and not enemy:
                                            r.hset(uid, 'daily', 0, {'daily_time': datetime.now().day})
                                            t = int(datetime.now().timestamp()) - int(r.hget(uid, 'daily_start'))
                                            r.hdel(uid, 'daily_start')
                                            if not r.hexists('daily', uid):
                                                msg2 = {"daily_wins": 0}
                                            else:
                                                msg2 = json.loads(r.hget('daily', uid).decode())
                                            msg2["daily_wins"] += 1
                                            msg2["completed"] = int(datetime.now().timestamp())
                                            msg2["time_used"] = t
                                            msg2["tries"] = try_n
                                            if 'username' in body['message'].get('from'):
                                                msg2["username"] = body['message'].get('from').get('username')
                                            r.hset('daily', uid, str(msg2).replace("'", '"'))
                                            salt = complete_daily(uid)
                                            if salt:
                                                msg += f'🧂 +{salt}\n\n'
                                        msg += results[2]
                                        r.hincrby('wins', uid, 1)

                                    bot.send_message(cid, msg, parse_mode='HTML')
                                    if enemy:
                                        r.hdel(uid, 'duel')
                                        r.hdel(enemy, 'duel')
                                        msg = f'{results[0]} - {correct}\n\n/wordle'
                                        if enemy != uid:
                                            bot.send_message(enemy, msg, parse_mode='HTML')
                                else:
                                    bot.send_sticker(cid, open(f'/tmp/{files[1]}', "rb"))
                                    if enemy and enemy != uid:
                                        bot.send_sticker(enemy, open(f'/tmp/{files[1]}', "rb"))
                            else:
                                msg = get_message(uid, 'opponents_turn')
                                bot.send_message(cid, msg)
                        else:
                            msg = get_message(uid, 'word_unavailable')
                            bot.send_message(cid, msg)
    except Exception as e:
        print(e)
