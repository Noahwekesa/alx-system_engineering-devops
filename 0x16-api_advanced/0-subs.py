#!/usr/bin/python3
""" Query calls Reddit API and returns the number of subscribers """
import requests


def number_of_subscribers(subreddit):
    """returns number of subs given a subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5 (by /u/COOLDOWNYOURPACE)"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    num_subs = response.json().get("data").get("subscribers")
    return num_subs
