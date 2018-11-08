from _collections import defaultdict
def longestSub(s):
    char_dict=[-1]*256
    longest=0
    m=0
    
    for i in range(len(s)):
        m=max(char_dict[ord(s[i])]+1,m)
        char_dict[ord(s[i])]=i
        longest=max(longest, i-m+1)
    
    return longest
    
s="abcabcbb"
print longestSub(s)