import sys

def isNameInTweet(names, tweet):
  # insert names into dictionary
  prev = None
  nametable = {}
  tweetwords = []
  for n in names:
    nametable[n] = True
  # tokenize tweet by word
  tweetwords = tweet.split()
  print tweetwords
  # combine words into pairs in order, lookup in dict
  for w in tweetwords:
    if not prev:
      prev = w
      continue
    print "looking for " + prev + " " + w
    if str(prev + " " + w) in nametable:
      return True
    prev = w
  return False 

def main():
  names = ['Katy Perry', 'Russell Brand', 'Russel Crowe']
  tweet = 'Katy Perry and Russel Brand make a nice couple!'
  print str(names) + " " + str(tweet) + " " +str( isNameInTweet(names, tweet))

if __name__ == "__main__":
  sys.exit(main())