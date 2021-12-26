class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if not curr.children[ord(c) - ord('a')]:
                curr.children[ord(c) - ord('a')] = TrieNode()
            curr = curr.children[ord(c) - ord('a')]
        curr.isWord = True

    def search(self, word: str) -> bool:
        node = self.root
        return self._searchMatch(word, node, 0)

    def _searchMatch(self, word, node, idx):
        if not node:
            return False
        if idx == len(word):
            return node.isWord

        if word[idx] != ".":
            child = node.children[ord(word[idx]) - ord('a')]
            return self._searchMatch(word, child, idx + 1)
        else:
            for child in node.children:
                if child and self._searchMatch(word, child, idx + 1):
                    return True
            return False


class TrieNode:

    def __init__(self):
        self.children = [None] * 26
        self.isWord = False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
