def do_twice(f,arg):
    f(arg)
    f(arg)

def print_once(arg):
    print(arg)

def do_four(f,arg):
    do_twice(f,arg)
    do_twice(f,arg)

def print_plus():
    print('+ - - - - '*4+'+')

def print_minus():
    print('|        '*4+'|')

def half():
    print_plus()
    do_four(print_once,'|         '*4+'|')

def grid():
    half()
    half()
    half()
    half()
    print_plus()

grid()
