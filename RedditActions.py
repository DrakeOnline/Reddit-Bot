# |========================================================|
# |    Title:      RedditActions                           |
# |    Author:     Drake G. Cummings                       |
# |    Purpose:    Consolidate Reddit methods              |
# |    Date:       April 18th, 2021                        |
# |========================================================|

from random import randint


def RandomVote(item):
    # Flip a coin
    chance = randint(1,10)

    if chance >= 5:
        item.upvote()
        return "Upvoted"
    else:
        item.downvote()
        return "Downvoted"


def RandomReply(item):
    # Flip a coin
    chance = randint(1,10)

    if chance >= 5:
        # Check if item is a post
        if not item.archived:
            item.reply("I could honestly not agree more, what a mature point you made.")
            # Printing
            return "Agreed"
    else:
        # Check if item is a post
        if not item.archived:
            item.reply("Wrong, wrong, wrong!!! >:( >:(")
            # Printing
            return "Disagreed"
