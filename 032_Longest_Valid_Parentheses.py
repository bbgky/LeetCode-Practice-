class Solution(object):
    def longestValidParentheses(self,s):
    """
    :type s : str
    :rtype :int
    """
    maxlen = 0
    left = -1
    stack = []
    for i in range(len(s)):
        if s[i]=='(':
            stack.append(i)
        else:
            if stack==[]:
                left=i
            else:
                stack.pop()
                if stack==[]:
                    maxlen = max(maxlen,i-left)
                else:
                    maxlen = max(maxlen,i-stack[-1])
    return maxlen


        