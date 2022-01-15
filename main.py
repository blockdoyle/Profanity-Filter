import marisa_trie, difflib

def importBlacklist(): # imports blacklisted words from 'blacklist.txt'
    file = open("blacklist.txt")
    return file.read().splitlines()

def convertToWhole(num): # converts float to integer
    return int(num * 100)

def getDifference(one,two): # gets the difference between 2 strings and returns as percentage
    difference = difflib.SequenceMatcher(None,one,two).ratio()
    return convertToWhole(difference)
    
def processString(txt): # Removes all punctuation from string
    specialChars = "!,.'\""
    for specialChars in specialChars:
        txt = txt.replace(specialChars, "")
    return txt

def findBlacklistWord(testWord,trie): # compares a word against similarities in trie, and returns if 85% or mroe match
    words = []
    for word in trie:
        if getDifference(testWord, word) > 85:
            words.append(word)
        else:
            continue
    return words

#TESTING CODE BLOCK    
blacklistWords = importBlacklist() # calls importBlacklist function

blacklistTrie = marisa_trie.Trie(blacklistWords) # takes the blacklistWords list and puts it into a marisa_trie trie

msg = processString("You are such a fucking asshole, you know that? Go fuck yourself cunt.".lower()).split()

for word in msg:
    print(findBlacklistWord(word, blacklistTrie.keys(word)))