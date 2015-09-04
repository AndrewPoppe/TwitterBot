from twython import Twython, TwythonError
import time

APP_KEY = 'YOUR KEY'
APP_SECRET = 'YOUR SECRET KEY'
OAUTH_TOKEN = 'YOUR TOKEN'
OAUTH_TOKEN_SECRET = 'YOUR SECRET TOKEN'

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

messages = ["I voted for #GoodMythicalMorning for the #Streamys!", "I voted for #TeensReact for the #Streamys!"]

secondsToWait = 432 # corresponds to 200 tweets per day. Max for the streamys is either 100 votes per day total or 100 votes per day per nominee. This will try to vote 100 times per day per the two nominees.

currentMessageNumber = 0
while True:
    thisMessage = messages[currentMessageNumber]
    print ("Tweeting:" + thisMessage)
    twitter.update_status(status=thisMessage)
    currentMessageNumber = abs(currentMessageNumber - 1)
    time.sleep(secondsToWait)
    