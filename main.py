import praw
from keep_alive import keep_alive
r = praw.Reddit('bot1')
keep_alive()

subreddit=r.subreddit("upvoteautomod")
for comment in subreddit.stream.comments(skip_existing=True):
    if comment.author.name=="AutoModerator":
        comment.reply("good bot")
        comment.upvote()
        comment.refresh()
        print("good botted")