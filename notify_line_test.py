import requests
import os

token = ''
msg = '\n動きを検知しました。\nメールを確認してください。'
payload = {'message': msg, 'stickerPackageId': 2, 'stickerId': 22}  # 送信メッセージ
url = 'https://notify-api.line.me/api/notify'
headers = {'Authorization': 'Bearer ' + token}
#files = {"imageFile":open('picture.png',"rb")}
fileName = os.path.abspath('picture.png')
#os.chdir(fileName)#画像保存先に移動
files = {'imageFile': open(fileName, 'rb')}
res = requests.post(url, params=payload, headers=headers)#,files=files)  # LINE NotifyへPOST
print(res)
print(files)
