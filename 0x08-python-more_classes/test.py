def print_string(print_symbol='#'):
    my_string = ''
    for i in range(5):
        for j in range(3):
            my_string += str(print_symbol)
        my_string += '\n'
    return my_string[:-1]

my_string = "#"
my_list = ['C', 'is fun']

print(print_string(my_list))
