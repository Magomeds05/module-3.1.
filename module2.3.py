call = 0

def count_calls():
    global call
    call += 1

count_calls()

def string_info(string):
    global call
    call = 5
    print(string)
    print(call)

string_info(15)
string_info('Fifteen')

def is_contains(string, list_to_search):
    print(string, list_to_search)

is_contains(True, False)
is_contains('Str', 'Str2')


