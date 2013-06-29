import sys
import json 

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    tweet_file = open(sys.argv[1])
    #hw()
    #lines(sent_file)
    #lines(tweet_file)
    
    get_tweet_line(tweet_file)


    

def get_tweet_line(tweet_file):
    # start with the tweet file 
    tweet_list = tweet_file.readlines()
    #json.load(tweet_list)

    tweet_score_dict = {}
    for i in range(len(tweet_list)):
	#print type(tweet_list[i])
	my_tweet_dict = json.loads(tweet_list[i])
	#print "\n", i
        if "entities" in my_tweet_dict.keys():
	  #print type(my_tweet_dict["entities"]["hashtags"])
	  #print my_tweet_dict["entities"]["hashtags"]
	  for w in my_tweet_dict["entities"]["hashtags"]:
	    #print type(my_tweet_dict["entities"]["hashtags"][w])
	     #print w.keys()
	     if w["text"] in tweet_score_dict.keys():
		tweet_score_dict[w["text"]] +=1
	     else: 
		tweet_score_dict[w["text"]] = 1

	#print i ,"\n"
    # Now need to go and sort the top hashtags
    #print tweet_score_dict

    score_this_list = []
    for item in tweet_score_dict: 
      score_this_list.append(tweet_score_dict[item])

    score_this_list.sort()
    #print score_this_list

    if len(score_this_list) >= 10: 
      max_number = 10
    else: 
      max_number = len(score_this_list)
 
    for top_ten in range(-1,-(max_number+1),-1): 
     for item in tweet_score_dict: 
      if (score_this_list[top_ten] == tweet_score_dict[item]):
        print item, float(tweet_score_dict[item])
        del tweet_score_dict[item]
        break 
     

    #print my_tweet_dict.keys()
    #print type(tweet_list)




if __name__ == '__main__':
    main()
