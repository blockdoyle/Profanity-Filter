import marisa_trie, enchant

def importBlacklist(): # imports blacklisted words from 'blacklist.txt'
    file = open("blacklist.txt")
    return file.read().splitlines()

blacklistWords = importBlacklist() # calls importBlacklist function

blacklistTrie = marisa_trie.Trie(blacklistWords) # takes the blacklistWords list and puts it into a marisa_trie trie

sentence = "".lower()

for word in sentence.split(): # checks each word in sentence if it's in the trie
    for entry in blacklistTrie.keys(word):
        if enchant.utils.levenshtein(word,entry) < 1:
            print("banned word", word)
    
print(blacklistTrie.keys(word))