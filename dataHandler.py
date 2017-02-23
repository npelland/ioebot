'''
getTweets(location, time)

getPhrase(location, time) -> 1-5 popular phrases at the time

getUsers(userIds) -> returns a list of user objects corresponding to the IDs sent
    userIDs :: A list containing at least one twitter user ID
'''

import tweepy

consumer_key = 'H5jr0sAGtmHS2EYM9KMNJflNP'
consumer_secret = 'X7rL5RcWIlfRHfQp1lr6AMOPE0ZGqIBdoaRCXTGmAPXGVmjpBW'
access_token = '826616430653227008-onbHLWk912tSBuRcutabkKk9fq10eVB'
access_token_secret = '65wd6VbcpbqsMDHixgysxMGQ31TEYGONnJOTpRmKJ68DH'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def getTweets(location, time):

    return 0

def getUsers(userIDs):
    users = []
    for user in userIDs:
        users.append(api.get_user(user))

    return users
