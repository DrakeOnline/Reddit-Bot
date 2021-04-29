# |========================================================|
# |    Title:      Reddit-Bot                              |
# |    Author:     Drake G. Cummings                       |
# |    Purpose:    A bot to do basic Reddit actions        |
# |    Date:       April 28th, 2021                        |
# |========================================================|

import praw
from secrets import client_id, client_secret, user_agent, username, password
import RedditActions


# Login with Authorized instance
reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent=user_agent,
                     username=username,
                     password=password)


# Proof that it works
subreddit = reddit.subreddit("NatureIsFuckingLit")
print()
for submission in subreddit.top(limit=1):
    print(f"r/NatureIsFuckingLit's top post: {submission.title}")
print()


# Acessing class subreddit
subreddit = reddit.subreddit("mechanicalMercs")

commentCount = 0
for submissions in subreddit.new(limit=11):
    # Title of post
    print("****Titles****")
    print(submissions.title)
    print(RedditActions.RandomVote(submissions))
    print()

    # Comments of post
    print("****Comments****")
    for comment in submissions.comments:
        # Check if comment was deleted
        if comment.body == "[deleted]":
            continue
        # To make sure bot doesn't reply to things twice if run again
        alreadyReplied = False
        print(comment.body)
        # Randomly upvote or downvote comments
        print(RedditActions.RandomVote(comment))
        print()

        # Check second layer of comments to see if already replied
        print("****2nd Layer Comments****")
        for secondLayerComment in comment.replies:
            print(secondLayerComment.body)

            # Check if I've been here
            if secondLayerComment.author == "DefNotDrakesBot":
                print("You already commented")
                commentCount += 1
                alreadyReplied = True
            print()

        # If haven't commented, comment
        # Reply criteria!
        if alreadyReplied is False:
            print(RedditActions.RandomReply(comment, commentCount))
            commentCount += 1
            print("Commented")
    print()
    print()
    print()
