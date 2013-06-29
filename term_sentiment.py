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

def get_sentiment(scores_dict,tweet_line,tsent_est_dict):
    # to determine the sentiment of each tweet 
    #get the line and return the sentiment of the line
    sentiment = 0
    count = 0
    #lines(score_file)
    word_list = tweet_line.split()
    for i in range(len(word_list)): 
      #see if word in scores_dict, if so add to sentiment, else add zero
      if word_list[i].lower() in scores_dict.keys():
       #print word_list[i].lower(), scores_dict[word_list[i].lower()]
       sentiment = sentiment + scores_dict[word_list[i].lower()]
       count = count + 1
      #else:
       #print word_list[i].lower()

    for i in range(len(word_list)):
      if count > 0:
       sent_tweet_avg = sentiment*1.0/count
      else: 
       sent_tweet_avg = 0

      if word_list[i].lower() not in scores_dict.keys():
       if word_list[i].lower() in tsent_est_dict.keys():
	tsent_est_dict[word_list[i].lower()].append(sent_tweet_avg)
       else: 
	tsent_est_dict[word_list[i].lower()] = [sent_tweet_avg]
    #print tsent_est_dict.keys()
    #print "sentiment:", sentiment, count, "\n"
    

def get_tweet_line(scores_dict, tweet_file):
    # start with the tweet file 
    tweet_list = tweet_file.readlines()
    #json.load(tweet_list)
   
    # for the term sentiment
    tsent_est_dict = {}
    tsent_est = {} # will be a dict with keys as terms and values as est

    for i in range(len(tweet_list)):
	#print type(tweet_list[i])
	my_tweet_dict = json.loads(tweet_list[i])
	#print "\n", i
	if "text" in my_tweet_dict.keys(): 
	 
  	 if "lang" in my_tweet_dict.keys(): 
	   if my_tweet_dict["lang"] == 'en':
	     #print my_tweet_dict["text"]
 	     get_sentiment(scores_dict,my_tweet_dict["text"],tsent_est_dict)
         else: 
	   # my_tweet_dict["text"]
 	   get_sentiment(scores_dict,my_tweet_dict["text"],tsent_est_dict)
	#print i ,"\n"

    #print tsent_est_dict, "\n"
    for item in tsent_est_dict: 
        list_score = tsent_est_dict[item]
     	est_score = sum(list_score)/float(len(list_score))
	tsent_est[item] = est_score
    #print tsent_est

    for item in tsent_est: 
      print item, tsent_est[item]
    #print my_tweet_dict.keys()
    #print type(tweet_list)




if __name__ == '__main__':
    main()
