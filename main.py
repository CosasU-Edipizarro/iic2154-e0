# Python modules
import json
from tkinter.tix import TCL_WINDOW_EVENTS

# PIP modules

# Local modules
import features

filename = 'dataset.json'
with open(filename) as file_object:
    dataset = [json.loads(line) for line in file_object]

if __name__ == '__main__':
    # Use features

    ## Use top retweeted feature
    top_retweeted = features.top_retweeted(dataset, n=10)
    print("Top retweeted:")
    for tweet in top_retweeted:
        print(tweet['retweetCount'])
    print("\n")

    ## Use top users feature
    ## Use top days by tweets feature
    top_weekdays_by_tweets = features.top_weekdays_by_tweets(dataset, n=7)
    print("Top weekdays by tweets:")
    for idx, day in enumerate(top_weekdays_by_tweets):
        print(f"{idx} - Day: {day[0]}, Tweets: {day[1]}")
    print("\n")

    ## Use top hashtags feature

    print("\n ### END OF CODE ### \n")
