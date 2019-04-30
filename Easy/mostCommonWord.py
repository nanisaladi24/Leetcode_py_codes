import re

def mostCommonWord(paragraph, banned):
    """
    :type paragraph: str
    :type banned: List[str]
    :rtype: str
    """
    bl=set(banned)


    regex = r"\w+"

    test_str = paragraph
    
    matches = re.finditer(regex, test_str, re.MULTILINE)

    k=[]

    for matchNum, match in enumerate(matches, start=1):

        sol="{match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group())
        k.append(sol.lower()) 
    
    myDict={}
    
    for i in k:
        if i not in bl:
            if i in myDict.keys():
                myDict[i]=myDict[i]+1
        
            else:
                myDict[i]=1
    
    myInd=max(myDict.values())
    
    for i in myDict.keys():
        if myDict[i]==myInd:
            return i
    
    return ""

myPara="Bob hit a ball, the hit BALL flew far after it was hit."

print mostCommonWord(myPara,["hit"])