from modules import scanner, helpers
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
    
    parser.add_argument(
        '-s',
        '--slug',
        help='Downloads plugin by slug and triggers analisys',
        type=str
    )

    args = parser.parse_args()

    if args.path or args.slug is None:
        argparse.ArgumentParser.print_usage(parser)
        exit(1)

    if args.slug:
        slug = args.slug
        path_to_plugin = helpers.download(slug, extract_zip_file=True)

    if args.path:
        path_to_plugin = args.path 

    scanner.scan(path_to_plugin)

if __name__ == '__main__':
    main()