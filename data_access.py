import config

import tweepy # tweepy is an API package that allows interaction with Twitter
from tweepy import OAuthHandler # OAuth = Open Authorization, a standard to
# allow interaction with a service (eg. Twitter) without exposing the user's password
# It uses access tokens that can be obtained from the registered Twitter app

auth = OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_secret)

api = tweepy.API(auth) # the variable 'api' now acts as an entry point to
# Twitter data

# to print top 3 tweets on the Twitter homepage:
for status in tweepy.Cursor(api.home_timeline).items(3):
    print(status.text)

# to store or process (here printed) tweets in JSON format:
#for status in tweepy.Cursor(api.home_timeline).items(3):
#    print(status._json)
