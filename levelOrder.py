__author__ = 'midhun'
import Queue

class Tnode:
    def __init__(self, v):
        self.val = v
        self.left = None
        self.right = None


class Tree:
    root = None

    def __init__(self):
        pass

    def insert(self, v):
        if self.root is None:
            self.root = Tnode(v)
        else:
            temp = self.root
            while temp is not None:
                if temp.val > v:
                    par = temp
                    temp = temp.left
                    dir = 0
                else:
                    par = temp
                    temp = temp.right
                    dir = 1
            if dir == 0:
                par.left = Tnode(v)
            else:
                par.right = Tnode(v)

    def lca(self, n1, n2):
        a = self.rec_lca(self.root, n1, n2)
        if a is not None:
            print(a.val)

    def lorder(self):
        q = Queue.Queue()
        q.put(self.root)
        q.put(Tnode(-99))
        while not q.empty():
            curr = q.get()
            if curr.val == -99 and not q.empty():
                q.put(curr)
                print("\n"),
            elif curr.val == -99 and q.empty():
                print("\n")
                return
            else:
                print(curr.val),
                if curr.left is not None:
                    q.put(curr.left)
                if curr.right is not None:
                    q.put(curr.right)

    def vorder(self):
        d = dict()
        self.rec_v_order(self.root, 0, d)
        print(d)
        for l in sorted(d.keys()):
            print (l, ' ', d[l])

    def rec_v_order(self, node, level, d):
        if node is None:
            return
        if node.left is not None:
            self.rec_v_order(node.left, level-1, d)
        if level in d:
            d[level].append(node.val)
        else:
            d[level] = list()
            d[level].append(node.val)
        if node.right is not None:
            self.rec_v_order(node.right, level+1, d)

    def rec_lca(self, curr, n1, n2):
        if curr is None:
            return None
        if (n1 < curr.val and curr.val < n2) or \
                (n2 < curr.val and curr.val < n1 )\
                or curr.val == n1 or curr.val == n2:
            return curr
        elif n1 < curr.val and n2 < curr.val:
            return self.rec_lca(curr.left,n1,n2)
        elif n1 > curr.val and n2 > curr.val:
            return self.rec_lca(curr.right,n1,n2)


if __name__ == '__main__':
    T = Tree()
    T.insert(5)
    T.insert(3)
    T.insert(1)
    T.insert(4)
    T.insert(7)
    T.insert(6)
    T.insert(8)
    #T.lorder()
    #T.vorder()
    T.lca(6, 8)