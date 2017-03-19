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
            #print("%s %s" %(counter, author))
            if author == me:
                #print('[main] not replying to self')
                continue


            text = comment.body
            words = findWords.findWords(text)

            for word in words:
                if counter > 3:
                    counter = 0
                else:
                    counter += 1
                word = word.replace(' ', '')
                result = cubify.cubify(word=word, subsqaures=(counter == 0))
                if (result):
                    #print('[main] attempting to reply')
                    comment.reply(result)
                    print('[main] replied to a comment')

                    break

    except:
        print('Unknown Crash')
        time.sleep(10)
