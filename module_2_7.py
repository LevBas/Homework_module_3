# Пункт 1
def print_params(a=1, b='строка', c=True):
    print(a, b, c)
print_params(b = 25)
print_params(c = [1, 2, 3])

# Пункт 2
values_list = ['Hi, people', 777, [34, 17, 12]]
values_dict = {'a': 'String', 'b': 5, 'c': False}
print_params(*values_list)
print_params(**values_dict)

# Пункт 3
values_list_2 = [[25, 12], 'apple']
print_params(*values_list_2, 42)