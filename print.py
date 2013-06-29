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
