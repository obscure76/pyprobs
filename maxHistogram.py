__author__ = 'obscure'
'''
s = [2,1,5,6,2,3]
'''

class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, h):
        st = []
        lenh = len(h)
        gAreaMax = 0
        i = 0
        while i < lenh :
            if not st or h[st[len(st)-1]] < h[i] :
                st.append(i)
                i += 1
            else :
                top = st.pop()
                if not st:
                    val = i
                else:
                    val = i - st[len(st)-1] -1
                lAreaMax = h[top] * val
                if lAreaMax > gAreaMax:
                    gAreaMax = lAreaMax
        while len(st) > 0 :
            top = st.pop()
            if not st:
                val = i
            else:
                val = i - st[len(st)-1] -1
            lAreaMax = h[top] * val
            if lAreaMax > gAreaMax:
                gAreaMax = lAreaMax
        print gAreaMax

if __name__ == '__main__':
    H = Solution()
    H.largestRectangleArea([2,1,5,6,2,3])