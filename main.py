import marisa_trie

def importBlacklist():
    file = open("blacklist.txt")
    return file.read().splitlines()

blacklistWords = importBlacklist()

trie = marisa_trie.Trie(blacklistWords)
print(trie.keys(""))