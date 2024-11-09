import requests
import os

success = 0
fails = 0

os.system("cls")
os.system("title ngl.link spammer ^| made by nismo1337 ^| sent: " + str(success) + " ^| fails: " + str(fails))

username = input("username:")
question = input("question:")

url = "https://ngl.link/api/submit"

headers = {
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Accept-Language": "en-GB,en;q=0.9",
    "Sec-Ch-Ua": "\"Not?A_Brand\";v=\"99\", \"Chromium\";v=\"130\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    "Accept": "*/*",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://ngl.link",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": f"https://ngl.link/{username}",
    "Accept-Encoding": "gzip, deflate, br",
    "Priority": "u=1, i"
}

payload = {
    "username": f"{username}",
    "question": f"{question}",
    "deviceId": "93967639-00e4-4e33-9be1-6a700a9ad489",
    "gameSlug": "",
    "referrer": ""
}


for _ in iter(int, 0.1):
    try:
        response = requests.post(url, headers=headers, data=payload)

        if response.status_code == 200:
            print("success")
            success = success + 1
            os.system("title ngl.link spammer ^| made by nismo1337 ^| sent: " + str(success) + " ^| fails: " + str(fails))
        
    except Exception as niggers:
        print("error: ", str(niggers))
        fails = fails + 1
        os.system("title ngl.link spammer ^| made by nismo1337 ^| sent: " + str(success) + " ^| fails: " + str(fails))