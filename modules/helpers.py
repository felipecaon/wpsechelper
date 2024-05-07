import sys, requests, io, zipfile
from colored import Fore, Style, Back
from modules.loader import Loader

def get_plugin_information(slug):
    response = requests.get(f"https://api.wordpress.org/plugins/info/1.2/?action=plugin_information&slug={slug}")
    if response.status_code == 200:
        data = response.json()
        if data['download_link']:
            download_link = data['download_link']
        
        active_installs = data['active_installs']
        version = data['version']
    else:
        sys.exit(f"{Fore.red}ERR: Failed to retrieve data. Status code: " + str(response.status_code) + f"{Style.reset}")

    return download_link, active_installs, version

def download(slug, extract_zip_file):
    plugin_download_link = ''
    plugin_source_code_path = ''

    plugin_download_link, plugin_active_installs, plugin_version = get_plugin_information(slug)
    
    print(f"\n")
    print(f"{Fore.white}{Back.green}-== Plugin Information ==-{Style.reset}")
    print(f"====> Slug: {Fore.green}{slug}{Style.reset}")
    print(f"====> Version: {Fore.green}{plugin_version}{Style.reset}")
    print(f"====> Installs: {Fore.green}{plugin_active_installs}+{Style.reset}")
    print(f"\n")
    print(f"{Fore.white}{Back.green}-== Plugin Code Analysys ==-{Style.reset}")

    if plugin_download_link:
        loader = Loader("Downloading plugin...", "Plugin downloaded!").start()
        response = requests.get(plugin_download_link)
        loader.stop()

        if extract_zip_file:
            if response.status_code == 200:
                zip_content = io.BytesIO(response.content)
                with zipfile.ZipFile(zip_content, 'r') as zip_ref:
                    zip_ref.extractall("source_codes")
                print(f"====> Source code path {Fore.green}source_codes/{slug}{Style.reset}\n")
                plugin_source_code_path = f"source_codes/{slug}"
            else:
                sys.exit(f"{Fore.red}ERR: Failed to download the file. Status code:" + response.status_code + f"{Style.reset}")

    return plugin_source_code_path