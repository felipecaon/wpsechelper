from helpers import scanner
import argparse

def main():
    parser = argparse.ArgumentParser(
        description='WPSecHelper - Find WordPress plugins security issues faster'
    )
    
    parser.add_argument(
        '-p',
        '--path',
        help='Path to plugin to analyze',
        type=str
    )

    parser.add_argument('--version', action='store_true', help="Show version number")

    args = parser.parse_args()

    if args.path is None:
        argparse.ArgumentParser.print_usage(parser)
        exit(1)

    scanner.scan(args)

if __name__ == '__main__':
    main()