import ctypes
import requests, random, string, base64, os
from pystyle import Colorate, Colors, Write
import time

os.system('cls')
headers = {
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
letters = ["a", "b","c", "d","e", "f","g", "h","i", "j","k", "l","m", "n", "o", "p","q", "r","s", "t","u", "v","w", "x","y", "z",]
userletters = ["j", "k", "w", "x","y", "z",]

def main():
    os.system("cls")
    print(Colorate.Horizontal(Colors.purple_to_red, f'''                                                                                                                  
┌─┐┌─┐┌─┐┌┬┐┬┌─┐┬ ┬  ┌─┐┌─┐┌┐┌   ┬  ┬┌─┐
└─┐├─┘│ │ │ │├┤ └┬┘  │ ┬├┤ │││ - └┐┌┘┌─┘
└─┘┴  └─┘ ┴ ┴└   ┴   └─┘└─┘┘└┘    └┘ └─┘ By Pąblo#4316  

Pąblo#4316 | https://github.com/palblo/SpotifyGen
    '''))
    print(Colorate.Horizontal(Colors.red_to_white, f'''NOTE #1: proxies may not work       
NOTE #2: to use proxies create a file named proxies.txt                
    '''))
    useproxies = Write.Input('use proxies? (yes / no)» ', Colors.red_to_purple, interval=0.00005)
    accountsnumber = int(Write.Input('how many accounts? » ', Colors.red_to_purple, interval=0.00005))
    print()
    generated = 0
    for i in range(accountsnumber):
        username = ''.join(random.choice(userletters) for _ in range(5))
        Email = ''.join(random.choice(string.ascii_letters) for _ in range(15)) + '@gmail.com'
        password = ''.join(random.choice(string.ascii_letters) for _ in range(10))
        payload = {
            'birth_day': '03',
            'birth_month': '04',
            'birth_year': '1994',
            'creation_flow': '',
            'creation_point': '"https://www.spotify.com/us/',
            'displayname': username,
            'username': username,
            'gender': random.choice(['male', 'female', 'neutral']),
            'iagree': '1',
            'key': 'a1e486e2729f46d6bb368d6b2bcda326',
            'platform': 'www',
            'referrer': 'https://www.spotify.com/us/',
            'send-email': '0',
            'thirdpartyemail': '0',
            'email': Email,
            'password': password,
            'password_repeat': password
        }
        if useproxies == 'yes':
            with open('proxies.txt') as f:
                lines = f.readlines()
            proxy = random.choice(lines)
            proxies = {
                'http': proxy,
            }
            response = requests.post('https://spclient.wg.spotify.com/signup/public/v1/account', headers=headers, data=payload, proxies=proxies)
            generated += 1
            generatedstr = str(generated)
            print(Colorate.Horizontal(Colors.green_to_red, '[GENERATED] email : ' + Email + ' | password : ' + password + ' | number : ' + generatedstr + ' | proxy : ' + proxy))
            file = open("generated.txt","a")
            file.write(Email + ":" + password + "\n")
            file.close
        if useproxies == 'no':
            response = requests.post('https://spclient.wg.spotify.com/signup/public/v1/account', headers=headers, data=payload)
            generated += 1
            generatedstr = str(generated)
            print(Colorate.Horizontal(Colors.green_to_red, '[GENERATED] email : ' + Email + ' | password : ' + password + ' | number : ' + generatedstr))
            file = open("generated.txt","a")
            file.write(Email + ":" + password + "\n")
            file.close
    time.sleep(2)
    main()
main()


                    
