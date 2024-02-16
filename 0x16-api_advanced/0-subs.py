#!/usr/bin/python3
""" Query Reddit API and returns the number of subs """
import requests


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "i will leave it black"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        return data["data"]["subscribers"]
    else:
        return 0
