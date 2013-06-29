import urllib 
import json 

response = urllib.urlopen("http://search.twitter.com/search.json?q=Apple") 
#print json.load(response)

pyresponse = json.load(response)

print type(pyresponse)
print pyresponse.keys()
#print pyresponse["results"]

#print type(pyresponse["results"])

results = pyresponse["results"]
print len(results)

print type(results[0])

#print results[0].keys()
print type(results[0]["text"])

for i in range(1):
  print results[i]["text"]
  print results[i]["iso_language_code"]
  #print results[i]



	 if "place" in my_tweet_dict.keys(): 
	   # type(my_tweet_dict["place"])
 	   #if (!isinstance(my_tweet_dict["place"], types.NoneType)):
	   if type(my_tweet_dict["place"]) is dict:
 	      print "Dicttype", my_tweet_dict["place"]["full_name"]
	      print my_tweet_dict["place"]["country_code"]
	 if "coordinates" in my_tweet_dict.keys():
	   print "coordinates"
	   print my_tweet_dict["coordinates"]
	 
