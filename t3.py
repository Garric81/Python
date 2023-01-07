
first_name = str (input())
last_name =  str (input())
answer = int ('Сколько вам  лет?')
age = int(input())
if 3 <= age <= 6:
    print('Вы ребёнок')
else:
  if 6 <= age <= 14:
        print('Вы Подросток')

print( first_name, last_name)

passwda = input ()
passwdb = input ()
if passwda == passwdb: # используем двойное равенство
    print('Пароль принят')
else:
    print('Пароль не принят')


num = int(input())
if num >= 18:
    print('Доступ разрешен')
else:
   print('Доступ запрещен') 
