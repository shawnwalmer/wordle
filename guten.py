import collections
from urllib import request

# Read input file, note the encoding is specified here
# It may be different in your text file
url = "http://www.gutenberg.org/files/2554/2554-0.txt"

response = request.urlopen(url)
raw = response.read()
a = raw.decode("utf-8-sig")

# Instantiate a dictionary, and for every word in the file,
# Add to the dictionary if it doesn't exist. If it does, increase the count.
wordcount = {}
# To eliminate duplicates, remember to split by punctuation, and use case demiliters.
for word in a.upper().split():
    word = word.replace(".","")
    word = word.replace(",","")
    word = word.replace(":","")
    word = word.replace("\"","")
    word = word.replace("!","")
    word = word.replace("â€œ","")
    word = word.replace("â€˜","")
    word = word.replace("*","")
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1

word_counter = collections.Counter(wordcount)

print(word_counter["WET"])