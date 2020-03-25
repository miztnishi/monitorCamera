
LINE_NOTIFY_MSG = '\n動きを検知しました。\nメールを確認してください。\n[LINEから送信]'
MAIL_SUBJECT = '動きを検知しました。{}'
MAIL_BODY = '動きを検知しました。\n写真を確認してください'

def getMsg(arg1, arg2):
    return arg1.format(arg2)
