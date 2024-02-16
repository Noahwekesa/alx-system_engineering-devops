#!/usr/bin/python3
""" calls the Reddit API and returns a list containing the titles
    of all hot articles
"""
import requests


def recurse(subreddit, hot_list=[], after="null"):
    """returns a list of all hot posts given a subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0 (/u/COOLDOWNYOURPACE)"}
    payload = {"limit": "100", "after": after}
    hot = requests.get(url, headers=headers, params=payload, allow_redirects=False)
    if hot.status_code != 200:
        return None
    else:
        posts = hot.json().get("data").get("children")
        hot_list += [post.get("data").get("title") for post in posts]
        after = hot.json().get("data").get("after")
        if after is not None:
            recurse(subreddit, hot_list, after)
        return hot_list
