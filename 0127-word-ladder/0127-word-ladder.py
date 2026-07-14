class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        seen=set(wordList)
        q=deque([(beginWord, 1)])
        while q:
            word, lev=q.popleft()
            if word==endWord: return lev
            for i in range(len(word)):
                for ch in "qwertyuiopasdfghjklzxcvbnm":
                    nxt=word[:i]+ch+word[i+1:]
                    if nxt in seen:
                        seen.remove(nxt)
                        q.append((nxt,lev+1))
        return 0