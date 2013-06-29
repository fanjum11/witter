import sys
import json 

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #hw()
    #lines(sent_file)
    #lines(tweet_file)
    scores_dict = sentiments(sent_file)
    
    get_tweet_line(scores_dict, tweet_file)

def sentiments(score_file):
    afinnfile = score_file
    scores = {} #initializing empty dictionary 
    for line in afinnfile: 
	term,score = line.split("\t")
	scores[term] = int(score)
    #print scores.items()
    return scores

def get_sentiment(scores_dict,tweet_line):
    # to determine the sentiment of each tweet 
    #get the line and return the sentiment of the line
    sentiment = 0
    #lines(score_file)
    word_list = tweet_line.split()
    for i in range(len(word_list)): 
      #see if word in scores_dict, if so add to sentiment, else add zero
      if word_list[i].lower() in scores_dict.keys():
       #print word_list[i].lower(), scores_dict[word_list[i].lower()]
       sentiment = sentiment + scores_dict[word_list[i].lower()]
    print sentiment
    

def get_tweet_line(scores_dict, tweet_file):
    # start with the tweet file 
    tweet_list = tweet_file.readlines()
    #json.load(tweet_list)

    for i in range(len(tweet_list)):
	#print type(tweet_list[i])
	my_tweet_dict = json.loads(tweet_list[i])
	#print "\n", i
	if "text" in my_tweet_dict.keys(): 
	 
  	 if "lang" in my_tweet_dict.keys(): 
	   if my_tweet_dict["lang"] == 'en':
	     #print my_tweet_dict["text"]
 	     get_sentiment(scores_dict,my_tweet_dict["text"])
         else: 
	   # my_tweet_dict["text"]
 	   get_sentiment(scores_dict,my_tweet_dict["text"])
	#print i ,"\n"

    #print my_tweet_dict.keys()
    #print type(tweet_list)




if __name__ == '__main__':
    main()
