def right_justify(Emmanuelle):
    Emmanuelle=part1+part2
    print(Emmanuelle)

part1=' '*70
part2='Emmanuelle'
right_justify('Emmanuelle')

def do_twice(f,arg):
    f(arg)
    f(arg)

def print_shalom():
    print('shalom')

def print_twice(arg):
    print(arg)
    print(arg)

def do_four(f, arg):
    do_twice(f, arg)
    do_twice(f,arg)

do_twice(print_twice,'shalom')
print(' ')

do_four(print_twice,'shalom')
