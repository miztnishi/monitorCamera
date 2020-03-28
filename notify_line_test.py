import requests
import os
import logging.config
import time
import message
import requests

logging.config.fileConfig('log.conf')
logger = logging.getLogger()

class SendLine:
    token = os.environ["LINE_ACCESS_TOKEN"]
    msg = message.LINE_NOTIFY_MSG

    def sendLine(self):
        logger.info('SendLineクラス処理開始。')
        try:
            payload = {'message': self.msg, 'stickerPackageId': 2, 'stickerId': 22}  # 送信メッセージ
            url = 'https://notify-api.line.me/api/notify'
            headers = {'Authorization': 'Bearer ' + self.token}

            res = requests.post(url, params=payload, headers=headers) # LINE NotifyへPOST
            print(res)
            logger.info('SendLineクラス処理を終了します。')
        except Exception as e:
            logger.error('SendLineクラスで処理が失敗しました。\n' + str(e))
            raise e
