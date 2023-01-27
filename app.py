import os
import time

import schedule
import tweepy
from dotenv import load_dotenv

# Load .env
load_dotenv()

# Set Twitter configuration
CONSUMER_KEY = os.environ.get("CONSUMER_KEY")
CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET")
ACCESS_KEY = os.environ.get("ACCESS_KEY")
ACCESS_SECRET = os.environ.get("ACCESS_SECRET")

# Configure Twitter client
client = tweepy.Client(
    consumer_key=CONSUMER_KEY,
    consumer_secret=CONSUMER_SECRET,
    access_token=ACCESS_KEY,
    access_token_secret=ACCESS_SECRET,
)

# Specify time, timezone and text to tweet
TIME = ""
TZ = ""
TEXT = ""

def main():
    # Schedule the task
    schedule.every().day.at(TIME, TZ).do(tweet)

    while True:
        schedule.run_pending()
        time.sleep(1)


def tweet():
    # Post the tweet
    response = client.create_tweet(text=TEXT)

    return response


if __name__ == "__main__":
    main()
