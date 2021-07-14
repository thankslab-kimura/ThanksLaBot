# coding: utf-8

import labs.TwitterLab as twitter
import labs.ComedyLab as comedy
import labs.ComicLab as comic
import labs.EncryptionLab as encryption
import labs.EnglishLab as english
import labs.MusicLab as music
import labs.SDGsLab as sdgs
import labs.SheenaLab as sheena

if __name__ == '__main__':

    #message = comedy.message()
    #message = comic.message()
    #message = encryption.message()
    #message = english.message()
    #message = music.message()
    #message = sdgs.message()
    message = sheena.message()

    if (len(message) > 0):

        twitter.tweet(message)
        print("コンテンツの作成に成功しました。処理を終了します。")

    else:
        print("ツイートするコンテンツがありません。処理を終了します。")
