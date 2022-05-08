import ctypes
from socket import close
from weakref import proxy
import requests, random, string, base64, os
from pystyle import Colorate, Colors, Write
import time

os.system('cls')

ctypes.windll.kernel32.SetConsoleTitleW(f"» Spotify Generator | 1.2 | Generated: 0/0")

print(Colorate.Vertical(Colors.purple_to_red, f'''
                                                                                                  
╔═╗╔═╗╔═╗╔╦╗╦╔═╗╦ ╦  ┌─┐┌─┐┌┐┌
╚═╗╠═╝║ ║ ║ ║╠╣ ╚╦╝  │ ┬├┤ │││
╚═╝╩  ╚═╝ ╩ ╩╚   ╩   └─┘└─┘┘└┘              
'''))

print(Colorate.Vertical(Colors.red_to_white, f'''                                                                                              
NOTE #1: proxies may not work       
NOTE #2: to use proxies create a file named proxies.txt  
         
'''))


useproxies = Write.Input('use proxies? (yes / no)» ', Colors.red_to_purple, interval=0.00005)
accountsnumber = int(Write.Input('how many accounts? » ', Colors.red_to_purple, interval=0.00005))
ctypes.windll.kernel32.SetConsoleTitleW(f"» Spotify Generator | 1.2 | Generated: 0/{accountsnumber}")
print()

accountsgenerated = 0

ctypes.windll.kernel32.SetConsoleTitleW(f"» Spotify Generator | 1.2 | Generated: {accountsgenerated}/{accountsnumber}")

for i in range(accountsnumber):
    accountsgenerated += 1
    def random_strings(char_num) -> str:
           return ''.join(random.choices(string.ascii_letters, k=char_num))

    class SpotifyGenerator:
        def __init__(self, username) -> None:
            file = open('accounts.txt','a')
            self.username = 'Gen-' + username
            file.write('username: ' + self.username + '\n')
            self.email = '{}{}@gmail.com'.format(self.username, random_strings(5))
            file.write('email: ' + self.email + '\n')
            self.password = base64.b64encode(username.encode()).decode()
            file.write('password: ' + self.password + '\n' + '\n')
            self.request_url = 'https://spclient.wg.spotify.com/signup/public/v1/account'
            self.headers = {
                'authority': 'spclient.wg.spotify.com',
                'sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
                'sec-ch-ua-mobile': '?0',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
                 'sec-ch-ua-platform': '"Windows"',
                'content-type': 'application/x-www-form-urlencoded',
                'accept': '*/*',
                'origin': 'https://www.spotify.com',
                'sec-fetch-site': 'same-site',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'referer': 'https://www.spotify.com/',
                'accept-language': 'en-US,en;q=0.9'
            }
            self.data = {
                'birth_day': '03',
                'birth_month': '04',
                'birth_year': '1994',
                'creation_flow': '',
                'creation_point': '"https://www.spotify.com/us/',
                'displayname': self.username,
                'username': self.username,
                'gender': random.choice(['male', 'female', 'neutral']),
                'iagree': '1',
                'key': 'a1e486e2729f46d6bb368d6b2bcda326',
                'platform': 'www',
                'referrer': 'https://www.spotify.com/us/',
                'send-email': '0',
                'thirdpartyemail': '0',
                'email': self.email,
                'password': self.password,
                'password_repeat': self.password
            }
            print(Colorate.Horizontal(Colors.red_to_purple, 'email: ' + self.email))
            print(Colorate.Horizontal(Colors.red_to_purple, 'password: ' + self.password))
            print(Colorate.Horizontal(Colors.red_to_purple, 'username: ' + self.username))

        def generate_account(self) -> str:
            if useproxies == 'yes':
                with open('proxies.txt') as f:
                    lines = f.readlines()
                proxy=random.choice(lines)
                proxies = {
                    'http': proxy,
                }
                raw_data = open('raw.txt','a')
                print(Colorate.Horizontal(Colors.red_to_purple, 'proxy: ' + proxy))
                r = requests.post(self.request_url, headers=self.headers, data=self.data, proxies=proxies)
                if 'login_token' in r.text:
                    raw_data.write(r.text + '\n' + '\n')
                    return r.text
                else:
                    ctypes.windll.kernel32.SetConsoleTitleW(f"» Spotify Generator | 1.2 | Generated: {accountsgenerated}/{accountsnumber}")
                    print(Colorate.Horizontal(Colors.red_to_purple, 'Failed to create account'))
                    input()
                    raise Exception()
            if useproxies == 'no':
                raw_data = open('raw.txt','a')
                print(Colorate.Horizontal(Colors.red_to_purple, 'proxy: ' + 'NONE'))
                r = requests.post(self.request_url, headers=self.headers, data=self.data)
                if 'login_token' in r.text:
                    raw_data.write(r.text + '\n' + '\n')
                    return r.text
                else:
                    ctypes.windll.kernel32.SetConsoleTitleW(f"» Spotify Generator | 1.2 | Generated: {accountsgenerated}/{accountsnumber}")
                    print(Colorate.Horizontal(Colors.red_to_white, 'Failed to create account'))
                    input()
                    raise Exception()

    if __name__ == "__main__":
        account_gen = SpotifyGenerator(username=random_strings(10))
        generated_account = account_gen.generate_account()
        print(Colorate.Horizontal(Colors.green_to_white, f"an account has been generated [{accountsgenerated}]"))
        ctypes.windll.kernel32.SetConsoleTitleW(f"» Spotify Generator | 1.2 | Generated: {accountsgenerated}/{accountsnumber}")
        print()

print(Colorate.Horizontal(Colors.green_to_white, 'enjoy!'))
input()
close