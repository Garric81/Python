age = int(input())  # ввод
if age <= 13:  # проверка условий
    print('детство')
elif 14 <= age <= 24:
    print('молодость')
elif  25 <= age <= 59:
    print('зрелость')
elif 60 <= age <= 120:
    print('старость')
else: # защита от неверных данных
    print('Неверные данные!')
