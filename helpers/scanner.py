import os, re
from prettytable import PrettyTable
from prettytable import SINGLE_BORDER

TABLE_TITLE = ("Action Name", "Function", "File")

ajax_hooks_table = PrettyTable(TABLE_TITLE, header_style="upper", title="AJAX HOOKS", align="l")
ajax_hooks_table.set_style(SINGLE_BORDER)

admin_actions_table = PrettyTable(TABLE_TITLE, header_style="upper", title="ADMIN ACTIONS", align="l")
admin_actions_table.set_style(SINGLE_BORDER)

admin_init_table = PrettyTable(TABLE_TITLE, header_style="upper", title="ADMIN INIT", align="l")
admin_init_table.set_style(SINGLE_BORDER)

shortnames_table = PrettyTable(TABLE_TITLE, header_style="upper", title="SHORTNAMES", align="l")
shortnames_table.set_style(SINGLE_BORDER)

general_information_table = PrettyTable(("Information", "Bool", "keywords"), header_style="upper", title="GENERAL INFORMATION", align="l")
general_information_table.set_style(SINGLE_BORDER)

def extract_ajax_hooks(file_content, file):
    regex_pattern = r"(add_action(\s{0,}\S{0,})\((\s{0,}\S{0,})(\"|')(wp_ajax_[a-zA-Z0-9_-]+))(?!{)(\"|')(\s{0,}\S{0,}),(.+)(\"|')(\s{0,})([a-zA-Z0-9_-]+)(\s{0,})(\"|')"
    matches = re.findall(pattern=regex_pattern, string=file_content)
    for match in matches:
        ajax_hook = match[4]
        function = match[10]
        ajax_hooks_table.add_row([ajax_hook, function, file])

def extract_admin_actions(file_content, file):
    regex_pattern = r"(add_action(\s{0,}\S{0,})\((\s{0,}\S{0,})(\"|')(admin_action_[a-zA-Z0-9_-]+))(?!{)(\"|')(\s{0,}\S{0,}),(.+)(\"|')(\s{0,})([a-zA-Z0-9_-]+)(\s{0,})(\"|')"
    matches = re.findall(pattern=regex_pattern, string=file_content)
    for match in matches:
        admin_action = match[4]
        function = match[10]
        admin_actions_table.add_row([admin_action, function, file])
        
def extract_admin_init(file_content, file):
    regex_pattern = r"(add_action(\s{0,}\S{0,})\((\s{0,}\S{0,})(\"|')(admin_init*?))(?!{)(\"|')(\s{0,}\S{0,}),(.+)(\"|')(\s{0,})([a-zA-Z0-9_-]+)(\s{0,})(\"|')"
    matches = re.findall(pattern=regex_pattern, string=file_content)
    for match in matches:
        admin_init = match[4]
        function = match[10]
        admin_init_table.add_row([admin_init, function, file])

def extract_shortnames(file_content, file):
    regex_pattern = r"(add_shortcode(\s{0,}\S{0,})\((\s{0,}\S{0,})(\"|')([a-zA-Z0-9_-]+))(?!{)(\"|')(\s{0,}\S{0,}),(.+)(\"|')(\s{0,})([a-zA-Z0-9_-]+)(\s{0,})(\"|')"
    matches = re.findall(pattern=regex_pattern, string=file_content)
    for match in matches:
        shortname = match[4]
        function = match[10]
        shortnames_table.add_row([shortname, function, file])

def check_if_has_rest_routes(file_content):
    regex_pattern = r"register_rest_route"
    match = re.findall(pattern=regex_pattern, string=file_content)
    if match:
        general_information_table.add_row(["Has custom REST endpoints", "yes", "register_rest_route"])

# Analyze the file and extract interesting information
def analyze(file_content, file):
    extract_ajax_hooks(file_content, file)
    extract_admin_actions(file_content, file)
    extract_admin_init(file_content, file)
    extract_shortnames(file_content, file)
    check_if_has_rest_routes(file_content)

def scan(args):
    
    path_to_plugin = args.path

    if not os.path.exists(path_to_plugin):
        print("Path does not exists, provide an existing path")
        exit(0)

    # Checks every file of the plugin
    # If the file is PHP, proceed to analysis
    for root, _, files in os.walk(path_to_plugin):
        for file in files:
            if file.endswith('.php'):
                file_path = os.path.join(root, file)
                file_content = open(file_path, mode="r", encoding="latin1").read()
                analyze(file_content, file)


    if len(ajax_hooks_table.rows):
        print(ajax_hooks_table)

    if len(admin_actions_table.rows):
        print(admin_actions_table)

    if len(admin_init_table.rows):
        print(admin_init_table)

    if len(shortnames_table.rows):
        print(shortnames_table)

    if len(general_information_table.rows):
        print(general_information_table)
