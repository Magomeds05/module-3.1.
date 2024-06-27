def print_params(a = 1 ,b = 'строка',c = True):
    print(a, b, c)


print_params(2,'число', False)
print_params(2,'строка')
print_params(0, 25, [1,2,3])
print_params()


values_list = [1, 'строка', True]
print_params(*values_list)
values_dict = {'a': 1,'b': 'строка','c': True}
print_params(**values_dict)


values_list_2 = [21,42]
print_params(*values_list_2, 42)


