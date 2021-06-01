#!/usr/bin/env python
# coding: utf-8

import tweepy
import labs.data.private.config as config

def tweet(content):
    
    # 各種キーを取得
    consumer_key = config.CONSUMER_KEY
    consumer_secret = config.CONSUMER_SECRET
    access_token = config.ACCESS_TOKEN
    access_token_secret = config.ACCESS_TOKEN_SECRET

    # Twitterオブジェクトの生成
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    # ツイートを投稿
    try:
        api.update_status(content)
        # print("ツイートに成功しました。")
    except tweepy.TweepError as e:
        print("ツイートに失敗しました : " + str(e))
