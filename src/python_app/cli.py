import argparse


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="python-app")
    parser.add_argument(
        "--version",
        action="store_true",
        help="show the application version and exit",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.version:
        from python_app import __version__

        print(__version__)
        return 0

    print("Python app is ready.")
    return 0
