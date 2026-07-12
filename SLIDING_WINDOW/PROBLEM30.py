#SUBSTRING WITH CONCATENATION OF ALL WORDS

from typing import List
from collections import Counter,defaultdict
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        #EDGE CASE
        if not s or not words:
            return []
        #BASIC INFORMATION
        word_len=len(words[0])
        word_count=len(words)
        #REQUIRED WORD FREQUENCIES
        required=Counter(words)
        #STORE ANSWER
        result=[]
        #TRY EVERY POSSIBLE STARTING OFFSET
        for start in range(word_len):
            #SLIDING WINDOW STATE
            left=start
            window=defaultdict(int)
            matched=0
            #MOVE RIGHT ONE WORD AT A TIME
            for right in range(start,len(s)-word_len+1,word_len):
                #CURRENT WORD
                word=s[right:right+word_len]
                #VALID WORD
                if word in required:
                    #ADD WORD
                    window[word]+=1
                    matched+=1
                    #REMOVE EXTRA OCCURRENCES
                    while window[word]>required[word]:
                        left_word=s[left:left+word_len]
                        window[left_word]-=1
                        matched-=1
                        left+=word_len
                    #FOUND VALID WINDOW
                    if matched==word_count:
                        result.append(left)
                        #SLIDE WINDOW FORWARD
                        left_word=s[left:left+word_len]
                        window[left_word]-=1
                        matched-=1
                        left+=word_len
                else:
                    #RESET WINDOW
                    window.clear()
                    matched=0
                    left=right+word_len
        return result
obj=Solution()
s="barfoothefoobarman"
words=["foo","bar"]
print(obj.findSubstring(s,words))