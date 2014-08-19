import ssl
import tweepy
import datetime
import time
import csv

from datetime import date

today=date.today()
d0 = date(2012, 4, 30)
diff=(today-d0)
counter=diff.days*140


f=open('pi10million.txt')
f.seek(counter, 0)
newStat=f.read(140)
f.close

CONSUMER_KEY="your key"
CONSUMER_SECRET="your key"

ACCESS_KEY = 'your key'
ACCESS_SECRET = 'your key'

auth1 = tweepy.auth.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth1.set_access_token(ACCESS_KEY,ACCESS_SECRET)

api = tweepy.API(auth1)

api.update_status(newStat)
