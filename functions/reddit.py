import logging
import praw
import secret as secret
import pandas as pd
import datetime


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

reddit = praw.Reddit(
    client_id=secret.reddit_client_id,
    client_secret=secret.reddit_client_secret,
    user_agent=secret.reddit_user_agent,
)

subreddit = reddit.subreddit("all")

posts = subreddit.top(time_filter="month", limit=100)

posts_dict = {
    "title": [],
    "score": [],
    "total_comments": [],
    "post_url": [],
    "datetime_utc": [],
}

# for post in posts:
#     posts_dict["title"].append(post.title)
#     posts_dict["score"].append(post.score)
#     posts_dict["total_comments"].append(post.num_comments)
#     posts_dict["post_url"].append(post.url)

#     datetime_utc = datetime.datetime.fromtimestamp(post.created)
#     posts_dict["datetime_utc"].append(datetime_utc)

# top_posts = pd.DataFrame(posts_dict)
