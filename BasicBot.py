"""
This script posts a tweet to Twitter using the Tweepy API.
"""

import tweepy

# Set up authentication with Twitter API
API_KEY = "Replace this with your api key from twitter"
API_SECRET = "Your API secret key"
ACCESS_TOKEN = "Your access token here"
ACCESS_TOKEN_SECRET = "Secret token here"

# Create API object
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Define message to tweet
TWEET = "Hello World" #replace hellow world with the tweet you want to post

# Post the tweet
api.update_status(TWEET)
