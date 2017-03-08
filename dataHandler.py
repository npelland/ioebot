'''
getTweets(location, time)

getRateLimitStatus(rateSection, rateItem) -> returns the remaining API calls for each different type of call
    rateSection :: one of: 'users', 'statuses', 'help', 'search'
    rateItem :: one of: third = ['profile_banner', 'suggestions/:slug/members', 'show/:id', 'suggestions', 'lookup', 'search',
                                'contributors', 'contributees', 'suggestions/:slug', mentions_timeline', 'lookup','show/:id',
                                'oembed', 'retweeters/ids', 'home_timeline', 'user_timeline','retweets/:id','retweets_of_me',
                                'privacy', 'tos', 'configuration', 'languages','tweets']

getTrendingTopics(location) -> returns a list of the top 10 trending topics for the region defined by the WOEID (Countries only)
    location :: WOEID number for the country that is desired

woeidLookup(location) -> returns the WOEID for the location parameter
    location :: A string containing a location e.g. 'Spain' or 'Des Moines, Iowa' or 'Foz de Iguazu, Parana, Brazil'

getUsers(userIds) -> returns a list of user objects corresponding to the IDs sent
    userIDs :: A list containing at least one twitter user ID
'''

import tweepy, yweather

consumer_key = 'H5jr0sAGtmHS2EYM9KMNJflNP'
consumer_secret = 'X7rL5RcWIlfRHfQp1lr6AMOPE0ZGqIBdoaRCXTGmAPXGVmjpBW'
access_token = '826616430653227008-onbHLWk912tSBuRcutabkKk9fq10eVB'
access_token_secret = '65wd6VbcpbqsMDHixgysxMGQ31TEYGONnJOTpRmKJ68DH'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
client = yweather.Client()

def getUsers(userIDs):
    users = []
    for user in userIDs:
        users.append(api.get_user(user))

    return users

def woeidLookup(location):
    woeid = client.fetch_woeid(location)

    return woeid

def getTrendingTopics(location):
    trends = api.trends_place(id=location)
    data = trends[0]
    trending = data['trends']
    names = [trend['name'] for trend in trending]
    trendsList = ' '.join(names).split()

    return trendsList

def getRateLimitStatus(rateSection, rateItem):
    data = api.rate_limit_status()
    # second = ['users', 'statuses', 'help', 'search']
    # third = ['/users/profile_banner', '/users/suggestions/:slug/members', '/users/show/:id', '/users/suggestions', '/users/lookup', '/users/search', '/users/contributors', '/users/contributees', '/users/suggestions/:slug', '/statuses/mentions_timeline', '/statuses/lookup','/statuses/show/:id', '/statuses/oembed', '/statuses/retweeters/ids', '/statuses/home_timeline', '/statuses/user_timeline','/statuses/retweets/:id', '/statuses/retweets_of_me', '/help/privacy', '/help/tos', '/help/configuration', '/help/languages','/search/tweets']

    return data['resources'][rateSection]['/' + rateSection + '/' + rateItem]['remaining']

#print(getTrendingTopics(woeidLookup('United States')))
#print(getRateLimitStatus('users', 'suggestions'))

