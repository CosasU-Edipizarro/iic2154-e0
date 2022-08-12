from collections import defaultdict

def top_users_by_tweets(dataset, n=10):
    """
    Return the top n users by tweets in the dataset.
    """
    users = defaultdict(lambda: 0, {})
    for tweet in dataset:
        users[tweet['user']['username']] += 1
    
    return sorted(users.items(), key=lambda user: user[1], reverse=True)[:n]
