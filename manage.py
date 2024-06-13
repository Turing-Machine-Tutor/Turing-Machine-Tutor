import sys
from os import system

def install():
    """Installs pip requirements"""
    system('pip install -r requirements.txt')

def freeze():
    """Updates requirements.txt with the requirements you currently have"""
    system('pip freeze > requirements.txt')

def lint():
    """Runs the linter (tool that enforces code style)"""
    system('black src')

if __name__ == '__main__':
    methods = [install, lint, freeze]
    method_dict = {m.__name__: m for m in methods}

    def display_methods():
        for m in methods:
            print(m.__name__)
            print(m.__doc__)

    argv = sys.argv
    if len(argv) > 1:
        method_name = argv[1]
    else:
        print('choose action: ')

        method_name = input()

    if method_name in method_dict:
        method = method_dict[method_name]
        method()
    else:
        print('method not found: ' + method_name)
        display_methods()


