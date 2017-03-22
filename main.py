'''
Module to start program
import GUI
'''

from streamListener import *

consumer_key = 'H5jr0sAGtmHS2EYM9KMNJflNP'
consumer_secret = 'X7rL5RcWIlfRHfQp1lr6AMOPE0ZGqIBdoaRCXTGmAPXGVmjpBW'
access_token = '826616430653227008-onbHLWk912tSBuRcutabkKk9fq10eVB'
access_token_secret = '65wd6VbcpbqsMDHixgysxMGQ31TEYGONnJOTpRmKJ68DH'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
client = yweather.Client()

myStreamListener = StreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=StreamListener())

myStream.filter(follow=['826616430653227008'])
