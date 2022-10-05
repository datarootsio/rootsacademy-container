from rootsacademy_container import printer


def main() -> int:
    exit_code = printer.say_hello()
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
