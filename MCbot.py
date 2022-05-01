import praw
import time
import random

reddit = praw.Reddit(client_id='client',
                     client_secret='secret',
                     user_agent='agent')