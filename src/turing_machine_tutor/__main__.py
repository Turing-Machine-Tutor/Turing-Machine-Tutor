import sys

from turing_machine_tutor.other_file import get_message

def in_venv():
    return sys.prefix != sys.base_prefix

def main():
    msg = get_message()
    print(msg)
    print("\n----\n")
    print("You have set up the env correctly!" if in_venv() else "Something is wrong, talk to Yuval")

if __name__ == '__main__':
    main()
