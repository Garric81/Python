#speed = int(input())
print("Система расчёта штрафов")
car_speed = 85
is_town = True
fine_for_20_to_40 = 500
fine_for_40_to_60 = 1000
fine_for_60_to_80 = 2000
fine_for_80_and_more = 5000
town_speed = 60
country_speed = 90
if is_town:
  over_speed = car_speed - town_speed
else:
  over_speed = car_speed - country_speed

if over_speed < 20:
  print("Скорость не превышена или превышена незначительно")
elif over_speed >= 20 and over_speed < 40:
  print("Штраф: " + str(fine_for_20_to_40))
elif over_speed >= 40 and over_speed < 60:
  print("Штраф: " + str(fine_for_40_to_60))
elif over_speed >= 60 and over_speed < 80:
  print("Штраф: " + str(fine_for_60_to_80))
elif over_speed >= 80:
  print("Штраф: " + str(fine_for_80_and_more))
