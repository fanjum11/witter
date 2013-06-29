import sys
import json 
import types



def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
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
      encoded_word = word_list[i].encode('utf-8')
      if encoded_word.lower() in scores_dict.keys():
       #print word_list[i].lower(), scores_dict[word_list[i].lower()]
       sentiment = sentiment + scores_dict[word_list[i].lower()]
    return sentiment
    

def get_tweet_line(scores_dict, tweet_file):
    # start with the tweet file 
    tweet_list = tweet_file.readlines()
    #json.load(tweet_list)

    state_dict = {} 

    for i in range(len(tweet_list)):
	#print type(tweet_list[i])
	my_tweet_dict = json.loads(tweet_list[i])
	#print "\n", i
	if "text" in my_tweet_dict.keys(): 

  	 if ("lang" in my_tweet_dict.keys()) & (type(my_tweet_dict["place"]) is dict): 
 	   
	   if (my_tweet_dict["lang"] == 'en') & (my_tweet_dict["place"]["country_code"] == 'US'):
	     #print "place is", my_tweet_dict["text"], 
	     #print "country", my_tweet_dict["place"]["country_code"]
	     state_list = (str(my_tweet_dict["place"]["full_name"])).split()
	     #print "state is", state_list, state_list[-1]
 	     tsentiment = get_sentiment(scores_dict,my_tweet_dict["text"])
	     set_state_sentiment(tsentiment,state_dict,state_list[-1])
         elif type(my_tweet_dict["place"]) is dict: 
	   if my_tweet_dict["place"]["country_code"] == 'US':
	     #print "state", my_tweet_dict["place"]["full_name"]
             state_list = (str(my_tweet_dict["place"]["full_name"])).split()
 	     tsentiment = get_sentiment(scores_dict,my_tweet_dict["text"])
             set_state_sentiment(tsentiment,state_dict,state_list[-1])
	 else: 
            #do nothing here since place is not dict. 
            i 
	#print i ,"\n"
    happiest_state = ''
    happiest_sent = -10000 
    for item in state_dict: 
       #list_sentiment = state_dict[item]
      stat_sen = sum(state_dict[item])/float(len(state_dict[item]))
      if (stat_sen > happiest_sent): 
        happiest_state = item
        happiest_sent = stat_sen
      #print item, stat_sen 
    print str(happiest_state)

def set_state_sentiment(sentiment,my_state_dict,tweet_state): 
       if tweet_state in my_state_dict.keys():
	my_state_dict[tweet_state].append(sentiment)
       else: 
	my_state_dict[tweet_state] = [sentiment]



if __name__ == '__main__':
    main()
