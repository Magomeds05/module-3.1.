call = 0

def count_calls(): #подсчет вызовов остальных функций.
    global call #глобальная переменная
    call += 1
    return call

def string_info(string):
    count_calls()
    a = len(string) #длины этой строки
    b = string.upper() #строку в верхнем регистре
    c = string.lower() #строку в нижнем регистре.
    return a, b, c

def is_contains(string, list_to_search):
    count_calls()
    for i in range(len(list_to_search)):
        if string.lower() in list_to_search[i].lower() or list_to_search[i].lower() in string.lower():
            return True
        else:
            return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # если строка находится в этом списке
print(is_contains('cycle', ['recycling', 'cyclic'])) # если отсутствует
print(call)



