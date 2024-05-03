# Made by bltondc | discord.gg/botter

import  requests,   concurrent.futures,   ctypes,  os

from    os          import system
from    colorama    import Fore, init
init()

os.system("cls")

def set_window_title(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)

class stats:
    checked = 0
    valid   = 0
    invalid = 0

set_window_title(f"Palatial Token Checker | Checked {stats.checked} | Valid {stats.valid} | Invalid {stats.invalid}")

def validate_token(token):
    headers = {
        "authority": "id.twitch.tv",
        "method": "GET",
        "path": "/oauth2/validate",
        "scheme": "https",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9",
        "Authorization": f"Bearer {token}",
        "Cache-Control": "no-cache",
        "Origin": "https://barrycarlyon.github.io",
        "Pragma": "no-cache",
        "Priority": "u=1, i",
        "Referer": "https://barrycarlyon.github.io/",
        "Sec-Ch-Ua": '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    }
    response = requests.get("https://id.twitch.tv/oauth2/validate", headers=headers)
    stats.checked += 1
    set_window_title(f"Palatial Token Checker | Checked {stats.checked} | Valid {stats.valid} | Invalid {stats.invalid}")
    if response.status_code == 200:
        stats.valid += 1
        res = response.json()
        username = res['login']
        user_id = res['user_id']
        print(f"[{Fore.GREEN}+{Fore.RESET}] Valid! | {token} | {username} | {user_id}")
        open('Checked/valid.txt', 'a').write(token + "\n")
        set_window_title(f"Palatial Token Checker | Checked {stats.checked} | Valid {stats.valid} | Invalid {stats.invalid}")
    else:
        stats.invalid += 1
        print(f"[{Fore.RED}-{Fore.RESET}] Invalid! | {token} ")
        open('Checked/invalid.txt', 'a').write(token + "\n")
        set_window_title(f"Palatial Token Checker | Checked {stats.checked} | Valid {stats.valid} | Invalid {stats.invalid}")

def CheckToken():
    with open("tokens.txt", "r") as file:
        tokens = file.read().splitlines()

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(validate_token, tokens)
    print(f"[{Fore.GREEN}+{Fore.RESET}] Checking Process has finished! Total Checked {stats.valid} Valid {stats.valid} Invalid {stats.invalid}")
    input(f"[{Fore.GREEN}+{Fore.RESET}] Press enter to exit")
CheckToken()