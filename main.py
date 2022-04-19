import tweepy
import config
import random
import time





# Authenticate to Twitter
auth = tweepy.OAuthHandler(config.API_KEY, config.API_KEY_SECRET)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)

# Create API object
api = tweepy.API(auth)

while True:
    with open("words.txt", "r") as file:
        all_words = file.read()
        words = list(map(str, all_words.split()))

        tweet = "7 random words every 7 minutes to plant sad tree for #NYCFC, 2nd most massiv club in the world " + str(random.choices(words, k=7)) + " | #RBNY | #GreenerGoals | @MLSWORKS"

        print(tweet)


        api.update_status(tweet)
        time.sleep(420)