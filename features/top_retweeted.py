def top_retweeted(dataset, n=10):
    """
    Return the top n tweets retweeted in the dataset.
    """
    return sorted(dataset, key=lambda tweet: tweet['retweetCount'], reverse=True)[:n]