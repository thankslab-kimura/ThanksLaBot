# coding: utf-8

import DateLab
from TwitterLab import tweet
from datetime import datetime
    
if __name__ == '__main__':
    
    now = datetime.now()
    message = DateLab.message(now)
    
    if (len(message) > 0):
        
        tweet(message)
        print("コンテンツの作成に成功しました。処理を終了します。")
        
    else:
        print("ツイートするコンテンツがありません。処理を終了します。")
