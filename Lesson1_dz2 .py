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




def calc():

    #numbers = [11, 13, 15, "семнадцать", "девятнадцать"]
    #print(numbers)
    #print("снова")
    #for value in numbers:
    #    print(f"итог {value}")
    ##for index in range(0, 16, 2):
    #   numbers.append(index)
    #print(numbers)

    invalid = 10
    text = 1
    invalid = invalid + text

    for value in range(0, 5):
        invalid = invalid - 1
        print(f"{invalid}")

    kub_numbers = []
    for index in range(1, 1001, 2):
        kub_numbers.append(index ** 3)
    summ = 0
    for value in kub_numbers:
        temp_summ = 0
        original_value = value
        for index in range(8,-1,-1):
            div_value = 10**index
            digit = value // div_value
            value = value % div_value
            temp_summ += digit
        if (temp_summ % 7) == 0:
            summ += original_value
    print(summ)



#result = ""
#while result != 'q':
    #result = input('Введите длительность:')
    #duration = int(result)
    #time_parse(duration)
calc()#duration)
