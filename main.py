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
    ## Use top days feature
    ## Use top hashtags feature

    print("\n ### END OF CODE ### \n")
