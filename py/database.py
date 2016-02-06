import skilstak.colors as c

def hello(name):
    '''Prints hello (your name) in cyan.'''
    print(c.cyan + 'hello, ' + name)

def vegas(message):
    ''' Flashes the message towards the user'''
    while True:
        print(c.clear + c.multi( 'Hello ' + message))


