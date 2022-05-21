import praw 
import os

reddit = praw.Reddit(client_id='A50qwu2QUzy0lKpsbI7evg',
                     client_secret='1XKUOioVjx5OhnPS-df_d2GxnRRBPA',
                     user_agent='<console:MAGNIFICENT_C:1.0>')

subreddit = reddit.subreddit("MagC_bot")

print("this bot now works")







'''
client_id = os.getenv('client_id')
client_secret = os.getenv('client_secret')
user_agent = os.getenv('user_agent')
'''

