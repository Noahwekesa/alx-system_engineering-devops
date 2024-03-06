#!/usr/bin/python3
"""calls the Reddit API and prints the titles of the first 10 hot posts"""

import requests


def top_ten(subreddit):
    """returns the first 10 hot posts given a subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0 (/u/COOLDOWNYOURPACE)"}
    payload = {"limit": "10"}
    response = requests.get(url, headers=headers, params=payload, allow_redirects=False)
    if response.status_code != 200:
        print("None")
    else:
        hot_list = response.json().get("data").get("children")
        hot_titles = [post.get("data").get("title") for post in hot_list]
        print(*hot_titles, sep="\n")
