def time_parse(duration):
    if duration < 60:
        print(f"{duration} сек")
    elif duration < 3600:
        minutes = duration // 60
        seconds = duration % 60
        print(f"{minutes} мин {seconds} сек")
    elif duration < 24*3600:
        hours = duration // 3600
        duration = duration - hours*3600
        minutes = duration // 60
        seconds = duration % 60
        print(f"{hours} час {minutes} мин {seconds} сек")
    else:
        days = duration // 86400
        duration = duration - days*86400
        hours = duration // 3600
        duration = duration - hours*3600
        minutes = duration // 60
        seconds = duration % 60
        print(f"{days} дн {hours} час {minutes} мин {seconds} сек")






result = ""
while result != 'q':
    result = input('Введите длительность:')
    duration = int(result)
    time_parse(duration)
