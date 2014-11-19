__author__ = 'obscure'


class Vertex:

    def __init__(self, ch):
        self.char = ch
        self.words = 0
        self.prefixes = 1
        self.edges = [None]*26


class Trie:

    def __init__(self):
        self.v = Vertex('')
        self.v.words = 1


    def addWord(self, v, word, l, r):
        ch = ord(word[l]) - ord('a')
        l += 1
        if v.edges[(ch)] is None:
            v.edges[(ch)] = Vertex(ch)
            if l == r:
                v.edges[(ch)].words += 1
            else:
                self.addWord(v.edges[ch], word, l, r)
        else:
            v.edges[(ch)].prefixes += 1
            if l == r:
                v.edges[(ch)].words += 1
            else:
                self.addWord(v.edges[(ch)], word, l, r)


    def countPrefixes(self, v, prefix, l, r):
        if l == r:
            print(v.prefixes)
        else:
            self.countPrefixes(v.edges[ord(prefix[l])-ord('a')],prefix,l+1,r)

    def countWords(self, v, word, l, r):
        if l == r:
            print(v.words)
        else:
            self.countWords(v.edges[ord(word[l])-ord('a')],word,l+1,r)


if __name__ == '__main__':
    root = Trie()
    root.addWord(root.v,'He',0,2)
    root.addWord(root.v,'Hi',0,2)
    root.addWord(root.v,'Hello',0,5)
    root.addWord(root.v,'Hell',0,4)
    root.countPrefixes(root.v,'He',0,2)
    root.countWords(root.v,'He',0,2)

