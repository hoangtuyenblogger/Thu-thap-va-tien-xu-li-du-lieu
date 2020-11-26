docA = "the quick brown fox jumps over the lazy dog and"
docB = "never jump over the lazy dog quickly"

bowA = docA.split(" ")
bowB = docB.split(" ")

#Create dictionary
word_dict = set(bowA).union(set(bowB))

wordDictA = dict.fromkeys(word_dict, 0)
wordDictB = dict.fromkeys(word_dict, 0)



print(wordDictA)
#count the word in bads
for word in bowA:
    wordDictA[word]+=1

for word in bowB:
    wordDictB[word]+=1

