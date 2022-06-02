from workflow.task.cmd_manager import parse


def main():
    while True:
        try:
            exp = input("Input factor calculation expression:")
            parse.deley(exp)
        except Exception:
            continue


if __name__ == '__main__':
    main()
