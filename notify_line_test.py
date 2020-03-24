import requests
import os
import logging.config
import time


logging.config.fileConfig('log.conf')
# ログの出力名を設定（1）
logger = logging.getLogger()

if __name__ == '__main__':
    while(True):
        token = ''
        msg = '\n動きを検知しました。\nメールを確認してください。'
        payload = {'message': msg, 'stickerPackageId': 2, 'stickerId': 22}  # 送信メッセージ
        url = 'https://notify-api.line.me/api/notify'
        headers = {'Authorization': 'Bearer ' + token}
        #files = {"imageFile":open('picture.png',"rb")}
        fileName = os.path.abspath('picture.png')
        #os.chdir(fileName)#画像保存先に移動
        #files = {'imageFile': open(fileName, 'rb')}
        res = requests.post(url, params=payload, headers=headers)#,files=files)  # LINE NotifyへPOST
        print(res)
        #print(files)

        logger.info('info')
        logger.warning('warning')
        time.sleep(3)
