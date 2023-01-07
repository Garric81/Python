messages_count = 100500
# Складывать строки и числа нельзя,
# потому придётся преобразовать messages_count в строку:
how_many_messages = 'У тебя ' + str(messages_count) + ' новых сообщений.'
print(how_many_messages)

# Будет напечатано:
# У тебя 100500 новых сообщений.