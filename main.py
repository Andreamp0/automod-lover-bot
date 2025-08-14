import praw 
from keep_alive import keep_alive
r = praw.Reddit('bot1') # the praw.ini file has been omitted for obvious security reasons 
keep_alive()

subreddit=r.subreddit("upvoteautomod")
for comment in subreddit.stream.comments(skip_existing=True):
    if comment.author.name=="AutoModerator":
        comment.reply("good bot")
        comment.upvote()
        print("good botted")
