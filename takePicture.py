import time
import picamera
import message
import logging.config

class TakePicture:

    logging.config.fileConfig('log.conf')
    logger = logging.getLogger()
    FILE_NAME = message.getMsgWithArg(message.FILE_NAME, datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
    def takePicture:
        logger.info('TakePictureクラス処理開始')
        try:
            with picamera.PiCamera() as camera:
             camera.resolution = (1024, 768)
             camera.start_preview()
             # Camera warm-up time
             time.sleep(2)
             cameras = camera.capture(FILE_NAME)
             logger.info('TakePictureクラス処理終了')
             return FILE_NAME
        except Exception e:
            logger.error('TakePictureクラス処理失敗\n' + str(e))
            raise e
