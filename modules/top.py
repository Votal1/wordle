import json
from datetime import datetime, date


def top_today(everyone, msg_err, msg_top):
    try:
        rating = {}
        for member in everyone:
            try:
                stats = json.loads(everyone[member])
                completed = int(stats['completed'])
                if 'username' in stats and date.fromtimestamp(completed) == date.today():
                    line = f'{stats["username"]}\n📊 {stats["tries"]} 🕰 {stats["time_used"]}\n'
                    rating.update({line: stats["tries"]})
            except:
                continue

        s_rating = sorted(rating, key=rating.get, reverse=False)

        new_s_rating = []
        for n in range(7):
            new_rating = {}
            for member in s_rating:
                stats = member.split()
                if int(stats[2]) == n:
                    ts = datetime.fromtimestamp(int(stats[4]))
                    t = ts.strftime("%M:%S")
                    if int(stats[4]) >= 3600:
                        t = '>60:00'
                    member = member.replace(f'{stats[3]} {stats[4]}', f'{stats[3]} {t}')
                    new_rating.update({member: int(stats[4])})
            s_rating2 = sorted(new_rating, key=new_rating.get, reverse=False)
            new_s_rating.extend(s_rating2)

        result = ''
        place = 1
        for n in new_s_rating:
            place1 = str(place) + '. '
            result += place1 + n
            place += 1
            if place == 11:
                break
        return f'{msg_top}\n\n{result}'

    except:
        return msg_err


def top_daily(everyone, msg_err, msg_top):
    try:
        rating = {}
        for member in everyone:
            try:
                stats = json.loads(everyone[member])
                line = f'{stats["username"]}\n🌞 {stats["daily_wins"]}\n'
                rating.update({line: stats["daily_wins"]})
            except:
                continue

        s_rating = sorted(rating, key=rating.get, reverse=True)

        result = ''
        place = 1
        for n in s_rating:
            place1 = str(place) + '. '
            result += place1 + n
            place += 1
            if place == 11:
                break
        return f'{msg_top}\n\n{result}'


    except:
        return 'Недостатньо інформації для створення рейтингу.'


def top_wins(everyone, everyone2, msg_err, msg_top):
    try:
        rating = {}
        for member in everyone:
            try:
                stats1 = int(everyone[member])
                stats2 = json.loads(everyone2[member])
                if 'username' in stats2:
                    line = f'{stats2["username"]}\n🏆 {stats1}\n'
                    rating.update({line: stats1})
            except:
                continue

        s_rating = sorted(rating, key=rating.get, reverse=True)

        result = ''
        place = 1
        for n in s_rating:
            place1 = str(place) + '. '
            result += place1 + n
            place += 1
            if place == 11:
                break
        return f'{msg_top}\n\n{result}'


    except:
        return msg_err
