# |========================================================|
# |    Title:      RedditActions                           |
# |    Author:     Drake G. Cummings                       |
# |    Purpose:    Consolidate Reddit methods              |
# |    Date:       April 18th, 2021                        |
# |========================================================|

from random import randint


# Vote Criteria!
"""
Takes a Reddit item, like a post or a comment, and
randomly decides to upvote or downvote it. Quite fickle
if you ask me.
"""


def RandomVote(item):
    # Flip a coin
    chance = randint(1, 10)

    if chance >= 5:
        item.upvote()
        return "Upvoted"
    else:
        item.downvote()
        return "Downvoted"


"""
Takes a reddit comment or post and makes a comment agreeing
or disagreeing, randomly. It makes sure it doesn't reply
to the same comment twice no matter how many times ran, and
deleted comment won't break it. It also trackes how many
comments it's made on the recent posts.
"""


def RandomReply(item, commentCount):
    # Flip a coin
    chance = randint(1, 10)

    if chance >= 5:
        # Check if item is a post
        if not item.archived:
            response = "I could honestly not agree more, what a "
            response += "mature point you made."
            response += f" I've made {commentCount} comments on this site"
            response += ", I know what I'm doing."
            item.reply(response)
            # Printing
            return "Agreed"
    else:
        # Check if item is a post
        if not item.archived:
            response = "Wrong, wrong, wrong!!! >:( >:("
            response += f" I've made {commentCount} comments on this site"
            response += ", I know what I'm doing."
            item.reply(response)
            # Printing
            return "Disagreed"
