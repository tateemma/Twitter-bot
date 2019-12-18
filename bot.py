#imports
import tweepy
import time

#you need to create a twitter developer account, apply to create an application and then obtain access keys that you will use here.
CONSUMER_KEY = "your consumer key"
CONSUMER_SECRET = "your consumer secret key"
ACCESS_KEY = "your access key"
ACCESS_SECRET = "your sccess secret"

#authorize
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#now you can tweet and go and check your twitter account to see if you have tweeted anything!
tweet = "Hi, guys. I will tell you about the greatest scientists of all time"
api.update_status(tweet)

#that was just a single tweet. You can create a list or dictionary or access stuff from a file and then tweet the items individually
Scientists = {"0": "Alhazen (965 – 1040): Sum of an integral power, Volume of a paraboloid, ‘Alhazen’s problem’ - the reflection of light from curved surfaces",
              "1": "Daniel Bernoulli (1700 – 1782): Bernoulli Effect, kinetic theory relating particle speeds in gases to temperature, the theory of risk",
              "2": "Albert Einstein (1879-1955) German,American: E=m*c2",
              "3": "Leonardo Pisano Bigollo (1170-1250) Italian: Fibonacci sequence",
              "4": "Pythagoras (570 – 495 BC) Greek: Pythagorean theorem",
              "5": "Alan Turing (1912-1954) British: Father of computer science, Turing machine, Turing test",
              "6": "Elizebeth Friedman (1892-1980) American: Breaking code, Cryptanalysis"
             }
             
for key, value in Scientists.items():
  tweet = value
  api.update_status(tweet)
  time.sleep(60)
  
#note that twitter only allows not more than 25 tweets per 15 minutes. You need to check their rules first to confirm!
#you can also read their documentation. you can retweet and do other cool stuff using a twitter  bot!
