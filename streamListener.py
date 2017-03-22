'''
This is for streaming data from Twitter
'''

from dataHandler import *

import tweepy

class StreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print_status(status.text);
