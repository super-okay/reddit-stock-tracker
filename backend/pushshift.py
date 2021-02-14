import requests
import json

base_comment_url = "https://api.pushshift.io/reddit/search/comment/?q={}&subreddit=wallstreetbets&after={}&size={}"
base_submission_url = "https://api.pushshift.io/reddit/search/submission/?q={}&subreddit=wallstreetbets&after={}&size={}"
ticker = "GME"
time = "1h"
size = "500"

full_comment_url = base_comment_url.format(ticker, time, size)
full_submission_url = base_submission_url.format(ticker, time, size)

# print(full_comment_url)
print(full_submission_url)

# response = requests.get(full_comment_url)
response = requests.get(full_submission_url)
data = response.json()
print(len(data["data"]))