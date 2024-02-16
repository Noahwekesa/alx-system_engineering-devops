#!/usr/bin/python3
"""
queries the Reddit API and prints the titles of the first 10 hot posts listed
"""

import requests


def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]
        for post in posts[:10]:
            title = post["data"]["title"]
            print(title)
    else:
        print(None)

    if response.status_code != 200 and response.status_code != 302:
        print("Invalid subreddit or API error.")
