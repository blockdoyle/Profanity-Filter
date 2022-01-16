import marisa_trie, difflib

def importBlacklist(blacklistFile): # imports blacklisted words from 'blacklist.txt'
    file = open(blacklistFile)
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
    for word in trie:
        if getDifference(testWord, word) > 85:
            return True
            continue
        else:
            continue
    return False

def incomingMessage(sentence): # Takes sentence variable and splits into list. Then checks if each word is blacklisted in blacklistTrie
    for word in sentence.split():
        if findBlacklistWord(word, blacklistTrie) == True:
            return "Banned"

if __name__ == "__main__":
    blacklistTrie = marisa_trie.Trie(importBlacklist("blacklist.txt")) # imports blacklist.txt and converts the list to trie