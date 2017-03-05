import cubify
import findWords
import praw
import obot
import time

reddit = praw.Reddit(client_id=obot.client_id,
                     client_secret=obot.client_secret,
                     user_agent=obot.user_agent,
                     username=obot.username,
                     password=obot.password)

me = reddit.user.me()


while True:
    try:
        subreddit = reddit.subreddit('all')
        comments = subreddit.stream.comments()

        counter = 0

        for comment in comments:

            author = comment.author
            counter += 1
            #print("%s %s" %(counter, author))
            if author == me:
                print('not replying to self')
                continue


            text = comment.body
            words = findWords.findWords(text)

            for word in words:
                word = word.replace(' ', '')
                result = cubify.cubify(word)
                if (result):
                    print('attempting to reply')
                    comment.reply(result)
                    print('replied to a comment')

                    break

    except:
        print('Fatal Crash')
        time.sleep(60)
