import requests
import json

base_submission_url = "https://api.pushshift.io/reddit/search/submission/?q={}&subreddit=wallstreetbets&after={}&size=500"

class Reddit:

    def num_subs(ticker, time):
        full_submission_url = base_submission_url.format(ticker, time)
        response = requests.get(full_submission_url)
        data = response.json()
        return len(data["data"])