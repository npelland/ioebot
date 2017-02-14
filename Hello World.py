import tweepy

#This application reads through the users timeline and prints their tweets to the timeline

consumer_key = 'H5jr0sAGtmHS2EYM9KMNJflNP'
consumer_secret = 'X7rL5RcWIlfRHfQp1lr6AMOPE0ZGqIBdoaRCXTGmAPXGVmjpBW'
access_token = '826616430653227008-onbHLWk912tSBuRcutabkKk9fq10eVB'
access_token_secret = '65wd6VbcpbqsMDHixgysxMGQ31TEYGONnJOTpRmKJ68DH'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text