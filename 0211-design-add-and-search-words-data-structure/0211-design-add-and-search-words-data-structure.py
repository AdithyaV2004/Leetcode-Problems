class TrieNode:
    def __init__(self):
        self.children={}
        self.isEnd=False

class WordDictionary:
    def __init__(self):
        self.root=TrieNode()

    def addWord(self, word: str) -> None:
        crawl=self.root
        for c in word:
            if c not in crawl.children:
                crawl.children[c]=TrieNode()
            crawl=crawl.children[c]
        crawl.isEnd=True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            crawl=root
            for i in range(j, len(word)):
                c=word[i]
                if c=='.':
                    for child in crawl.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if c not in crawl.children:
                        return False
                    crawl=crawl.children[c]
            return crawl.isEnd
        return dfs(0, self.root)




# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)