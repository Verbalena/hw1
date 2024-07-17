calls = 0
def count_calls():
    global calls
    calls += 1
    return
def string_info(string):
    count_calls()
    string = str(input('Введи строку: '))
    str_len = str(len(string))  # ввела переменные: для подсчета длины строки,
    str_upp = string.upper()  # перевода строки в верхний регистр
    str_low = string.lower()  # перевода строки в нижний регистр
    rezalt = (int(str_len), str_upp, str_low)  # кортеж
    return rezalt
print(string_info(''))        # вызвала функцию string_info()
def is_contains(string, list_to_search):
    count_calls()
    for string in list_to_search:
        if string.lower() == string.lower():
            return True
        else:
            return False

print(is_contains('Urban', ['ban', 'Banan', 'urban']))
count_calls()
print(calls)
