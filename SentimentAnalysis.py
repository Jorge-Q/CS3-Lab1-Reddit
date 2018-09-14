#Created by:Jorge Quiñonez
#Last Modified: September 13, 2018
#Assignment: Lab 1 (Option B)

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import praw

reddit = praw.Reddit(client_secret='AjxVzMfBH8D52ABZii1htjdy1KA',
                     client_id='lbxQZ76M-mFcew',
                     user_agent='Jorge9898'
                     )


nltk.download('vader_lexicon')
sid = SentimentIntensityAnalyzer()


def get_text_negative_proba(text):
   return sid.polarity_scores(text)['neg']


def get_text_neutral_proba(text):
   return sid.polarity_scores(text)['neu']


def get_text_positive_proba(text):
   return sid.polarity_scores(text)['pos']


def get_submission_comments(url):
    submission = reddit.submission(url=url)
    submission.comments.replace_more()

    return submission.comments


#Method that places a comment into either the positive, negative, or neutral list
def place_in_list(comment, positive_list, negative_list, neutral_list):
    amount_positive = get_text_positive_proba(comment)
    amount_negative = get_text_negative_proba(comment)
    amount_neutral = get_text_neutral_proba(comment)
    if amount_positive >= amount_negative and amount_positive >= amount_neutral:
        positive_list.append(comment)
    elif amount_negative >= amount_positive and amount_negative >= amount_neutral:
        negative_list.append(comment)
    elif amount_neutral >= amount_positive and amount_neutral >= amount_negative:
        neutral_list.append(comment)


def process_comments(comments, positive_list, negative_list, neutral_list):
    for i in range(len(comments)):
        place_in_list(comments[i].body, positive_list, negative_list, neutral_list) #Placing the comment into a list
        process_comments(comments[i].replies, positive_list, negative_list, neutral_list) #Recursive call onto itself


def main():
    #Test 1
    #This thread was the one given to us in the instructions of the lab
    comments = get_submission_comments('https://www.reddit.com/r/learnprogramming/comments/5w50g5/eli5_what_is_recursion/')
    positive_list = []
    negative_list = []
    neutral_list = []
    for i in range(len(comments)):
        place_in_list(comments[i].body, positive_list, negative_list, neutral_list)
        process_comments(comments[i].replies, positive_list, negative_list, neutral_list)

    print('*******************************************')
    print('The following are from the post on reddit regarding recursion:')
    print('Positive comments list:')
    print(len(positive_list))
    print(positive_list)
    print('Negative comments list:')
    print(len(negative_list))
    print(negative_list)
    print('Neutral comments list:')
    print(len(neutral_list))
    print(neutral_list)

    #Test 2
    #I chose this thread to test my program because it is a post that is constantly changing since it is trending
    comments2 = get_submission_comments('https://www.reddit.com/r/DunderMifflin/comments/9fhrok/old_but_gold/')
    positive_list = []
    negative_list = []
    neutral_list = []
    for i in range(len(comments2)):
        place_in_list(comments2[i].body, positive_list, negative_list, neutral_list)
        process_comments(comments2[i].replies, positive_list, negative_list, neutral_list)
    print('*******************************************')
    print('The following are from the post on reddit regarding The Office:')
    print('Positive comments list:')
    print(len(positive_list))
    print(positive_list)
    print('Negative comments list:')
    print(len(negative_list))
    print(negative_list)
    print('Neutral comments list:')
    print(len(neutral_list))
    print(neutral_list)

    #Test 3
    #I chose this thread to test my program because it is believed to be a controversial post, and it has a vast number of comments
    comments3 = get_submission_comments('https://www.reddit.com/r/IAmA/comments/2s7obx/im_the_ceo_of_renault_and_nissan_and_were_making/')
    positive_list = []
    negative_list = []
    neutral_list = []
    for i in range(len(comments3)):
        place_in_list(comments3[i].body, positive_list, negative_list, neutral_list)
        process_comments(comments3[i].replies, positive_list, negative_list, neutral_list)
    print('*******************************************')
    print('The following comments are from a reddit MIA of the CEO of Renault and Nissan')
    print('Positive comments list:')
    print(len(positive_list))
    print(positive_list)
    print('Negative comments list:')
    print(len(negative_list))
    print(negative_list)
    print('Neutral comments list:')
    print(len(neutral_list))
    print(neutral_list)

main()
