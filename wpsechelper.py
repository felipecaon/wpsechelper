from modules import scanner, helpers
import argparse, shutil, os

_PATH_OF_PLUGIN_SOURCE_CODES = "source_codes"

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

    parser.add_argument(
        '-d',
        '--delete',
        help=f'Deletes {_PATH_OF_PLUGIN_SOURCE_CODES} folder before analyzing new plugin',
        action='store_true'
    )

    args = parser.parse_args()

    if not args.path and not args.slug:
        argparse.ArgumentParser.print_usage(parser)
        exit(0)

    if args.delete:
        if os.path.exists(_PATH_OF_PLUGIN_SOURCE_CODES):
            shutil.rmtree(_PATH_OF_PLUGIN_SOURCE_CODES)

    if args.slug:
        slug = args.slug
        path_to_plugin = helpers.download(slug, extract_zip_file=True)

    if args.path:
        path_to_plugin = args.path 

    scanner.scan(path_to_plugin)

if __name__ == '__main__':
    main()