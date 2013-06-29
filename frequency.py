import sys
import json 


def main():
    tweet_file = open(sys.argv[1])
    get_tweet_lines(tweet_file)


def get_frequency(tweet_line,word_freq_dict):
    # to determine the frequency of words in the tweet
    # and add to all the other tweets considered

    word_list = tweet_line.split()
    for i in range(len(word_list)): 
      if word_list[i].lower() in word_freq_dict.keys():
	word_freq_dict[word_list[i].lower()] +=1
      else: 
	word_freq_dict[word_list[i].lower()] = 1
    

def get_tweet_lines(tweet_file):
    # start with the tweet file 
    tweet_list = tweet_file.readlines()
    #json.load(tweet_list)
   
    # for the term sentiment
    word_freq_dict = {}

    for i in range(len(tweet_list)):
	#print type(tweet_list[i])
	my_tweet_dict = json.loads(tweet_list[i])
	#print "\n", i
	if "text" in my_tweet_dict.keys(): 
	 
  	 if "lang" in my_tweet_dict.keys(): 
	   if my_tweet_dict["lang"] == 'en':
	     #print my_tweet_dict["text"]
 	     get_frequency(my_tweet_dict["text"],word_freq_dict)
         else: 
	   # my_tweet_dict["text"]
 	   get_frequency(my_tweet_dict["text"],word_freq_dict)
	#print i ,"\n"

    #print word_freq_dict

    total_terms = 0.
    word_relative_freq = {}
    for item in word_freq_dict: 
      total_terms += word_freq_dict[item] 
      #print item, word_freq_dict[item]

    #print "total terms" , total_terms
    for item in word_freq_dict: 
      word_relative_freq[item] = word_freq_dict[item]/float(total_terms)
      print item, word_relative_freq[item]

if __name__ == '__main__':
    main()
