import praw
from dotenv import load_dotenv
import os

# Initialize Reddit API client
load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT")
)

def fetch_posts(subreddit_name):
    subreddit = reddit.subreddit(subreddit_name)
    
    # Fetch the top 10 hot posts
    print("Fetching posts from /r/stocks...\n")
    for post in subreddit.hot(limit=10):  # You can use .new(), .top(), etc.
        upvotes = post.ups
        score = post.score
        downvotes = upvotes - score  # Calculate downvotes
        
        print(f"Title: {post.title}")
        print(f"Author: {post.author}")
        print(f"Score: {score}")
        print(f"Upvotes: {upvotes}")  # Upvotes
        print(f"Downvotes: {downvotes}")  # Calculated Downvotes
        print(f"Comments: {post.num_comments}")
        print(f"URL: {post.url}\n")

    # Ask user if they want to fetch next 10 posts
    next_fetch = input("Do you want to fetch the next 10 posts? (yes/no): ").strip().lower()
    if next_fetch == 'yes':
        fetch_posts(subreddit_name)
    else:
        print("Exiting the script. Thank you!")

# Fetch posts from the "stocks" subreddit
fetch_posts("stocks")
