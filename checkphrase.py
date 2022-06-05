# Print each word in the phrase that appears immediately before the target word
#

phrase = "Now is the time for all good men to come to the aid of their country"
target = "to"
wordlist = phrase.split()
for index, word in enumerate(wordlist):
    if word == target and index != 0:
        print(wordlist[index - 1])
