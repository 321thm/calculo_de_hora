# Importa uma função de uma outra pasta
import funcoes_uteis as fu


def add_time(start, duration, day=False):
    # Dias da semana
    days = {
        1: 'Monday',
        2: 'Tuesday',
        3: 'Wednesday',
        4: 'Thursday',
        5: 'Friday',
        6: 'Saturday',
        7: 'Sunday'
    }
    # Lê os valores da hora, minuto e periodo do dia que inicia
    hour_s = ''
    division_s = list(start)

    for number in division_s:
        if fu.isnumber(number):
            hour_s += number
        else:
            break

    local_s = start.find(':')
    minute_s = division_s[local_s + 1] + division_s[local_s + 2]
    local2_s = start.find(' ')
    period_initial = division_s[local2_s + 1] + division_s[local2_s + 2]
    hour_s = int(hour_s)
    minute_s = int(minute_s)

    if period_initial == 'PM' and hour_s < 12:
        hour_s = hour_s + 12
    elif period_initial == 'AM' and hour_s == 12:
        hour_s = 0

    # Lê os valores da hora, minuto e periodo do dia que é somado
    hour_d = ''
    division_d = list(duration)

    for number in division_d:
        if fu.isnumber(number):
            hour_d += number
        else:
            break

    local_d = duration.find(':')
    minute_d = division_d[local_d + 1] + division_d[local_d + 2]
    local2_d = duration.find(' ')
    hour_d = int(hour_d)
    minute_d = int(minute_d)

    # Faz o calculo
    hour_end = hour_s + hour_d
    minute_end = None

    if minute_s + minute_d >= 60:
        minute_end = minute_s + minute_d - 60
        hour_end += 1
    else:
        minute_end = minute_s + minute_d
    period_end = None
    days_later = 0

    if hour_end == 0:
        period_end = 'AM'
        hour_end = 12
    elif hour_end < 12:
        period_end = 'AM'
    elif hour_end == 12:
        period_end = 'PM'
    elif hour_end < 24:
        period_end = 'PM'
        hour_end = hour_end - 12
    else:
        while hour_end >= 24:
            hour_end -= 24
            days_later += 1
        if hour_end == 0:
            period_end = 'AM'
            hour_end = 12
        elif hour_end < 12:
            period_end = 'AM'
        elif hour_end == 12:
            period_end = 'PM'
        else:
            period_end = 'PM'
            hour_end = hour_end - 12

    if day:
        if days_later > 0:
            day_end = None

            if fu.get_key(fu.first_letter_upper(day), days) + days_later <= 7:
                day_end = days[fu.get_key(fu.first_letter_upper(day), days) + days_later]
            else:
                loop = 0
                loop2 = fu.get_key(fu.first_letter_upper(day), days)
                while loop <= days_later:
                    if loop2 > 7:
                        loop2 = 1
                    day_end = days[loop2]
                    loop += 1
                    loop2 += 1

            if len(str(minute_end)) == 1:
                minute_end = f'0{minute_end}'
            if days_later == 1:
                return f'{hour_end}:{minute_end} {period_end}, {day_end} (next day)'
            else:
                return f'{hour_end}:{minute_end} {period_end}, {day_end} ({days_later} days later)'
        else:
            if len(str(minute_end)) == 1:
                minute_end = f'0{minute_end}'
            return f'{hour_end}:{minute_end} {period_end}, {day}'
    else:
        if days_later > 0:

            if len(str(minute_end)) == 1:
                minute_end = f'0{minute_end}'
            if days_later == 1:
                return f'{hour_end}:{minute_end} {period_end} (next day)'
            else:
                return f'{hour_end}:{minute_end} {period_end} ({days_later} days later)'
        else:
            if len(str(minute_end)) == 1:
                minute_end = f'0{minute_end}'
            return f'{hour_end}:{minute_end} {period_end}'
