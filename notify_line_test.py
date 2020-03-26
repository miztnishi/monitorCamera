import requests
import os
import logging.config
import time
import message
import requests

logging.config.fileConfig('log.conf')
# ログの出力名を設定（1）
logger = logging.getLogger()

class SendLine:
    token = os.environ["LINE_ACCESS_TOKEN"]
    msg = message.LINE_NOTIFY_MSG

    def sendLine(self):
        payload = {'message': self.msg, 'stickerPackageId': 2, 'stickerId': 22}  # 送信メッセージ
        url = 'https://notify-api.line.me/api/notify'
        headers = {'Authorization': 'Bearer ' + self.token}
        #files = {"imageFile":open('picture.png',"rb")}
        fileName = os.path.abspath('picture.png')
        #os.chdir(fileName)#画像保存先に移動
        #files = {'imageFile': open(fileName, 'rb')}
        res = requests.post(url, params=payload, headers=headers)#,files=files)  # LINE NotifyへPOST
        print(res)

if __name__ == '__main__':
    sd = SendLine()
    sd.sendLine()
