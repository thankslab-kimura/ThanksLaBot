# coding: utf-8

from labs.TwitterLab import tweet
import labs.SDGsLab as SDGs
import labs.ComedyLab as Comedy
    
if __name__ == '__main__':
    
    #message = SDGs.message()
    message = Comedy.message()
    
    if (len(message) > 0):
        
        tweet(message)
        print("コンテンツの作成に成功しました。処理を終了します。")
        
    else:
        print("ツイートするコンテンツがありません。処理を終了します。")
