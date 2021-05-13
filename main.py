import requests
def mc():
    print("Please enter your minecraft name here")
    token = input("> ")
    f= open('info.txt', 'w')
    f.writelines("Loading...")
    f.writelines('.\n')
    f.writelines(f'MC USER: {token}')
    f.writelines('.\n')




def mcusename():
    try:
        f = open('info.txt', 'w')
        print("Send minecraft username here: ")
        token = input("> ")
        names = []
        names.clear()
        req = requests.get(f'https://playerdb.co/api/player/minecraft/{token}')
        if 'code":"player.found"' in req.text:
            f.writelines(f"**MC INFORMATION | {token}**",)
            f.writelines('.\n')
            f.writelines(f"**Full UUID:**{req.json()['data']['player']['id']}")
            f.writelines('.\n')
            f.writelines(f"**Trimmed UUID:**{req.json()['data']['player']['raw_id']}")
            f.writelines('.\n')
            for name in req.json()['data']['player']['meta']['name_history']:
                names.append(name['name'])
            f.writelines(f"**Past Usernames**({len(names)}): {names}")
            f.writelines('.\n')
            f.writelines("https://crafatar.com/avatars/" + f"{req.json()['data']['player']['id']}")
    except Exception as e:
        f.writelines(f"Error occurred: {e}")


mcusename()