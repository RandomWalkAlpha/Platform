from cmd_manager import parse


def main():
    while True:
        try:
            exp = input("Input factor calculation expression:")
            parse.delay(exp)
        except Exception:
            continue


"""
This file is used to input the factor expression which is to be evaluated.
"""
if __name__ == '__main__':
    main()
