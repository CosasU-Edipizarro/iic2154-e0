from collections import defaultdict
from datetime import datetime

def top_weekdays_by_tweets(dataset, n=7):
    """
    Return the top n days by tweets in the dataset.
    """
    days = defaultdict(lambda: 0, {})
    for tweet in dataset:
        date = datetime.strptime(tweet['date'], '%Y-%m-%dT%H:%M:%S%z').isoweekday()
        fechas = {
            1: 'Lunes',
            2: 'Martes',
            3: 'Miercoles',
            4: 'Jueves',
            5: 'Viernes',
            6: 'Sabado',
            7: 'Domingo'
        }
        days[fechas[date]] += 1

    return sorted(days.items(), key=lambda day: day[1], reverse=True)[:n]
