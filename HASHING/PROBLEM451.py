#SORT THE CHARACTERS BY FREQUENCY

from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        #FIND COMMON DIGITS
        freq=Counter(s)
        #SORT CHARACTERS BY FREQUENCY (HIGHEST ORDER) 
        chars=sorted(freq,key=freq.get,reverse=True)
        #STORE THE FINAL ANSWER
        result=""
        #ADD EACH CHARACTERS ACCORDING TO ITS FREQUENCIES
        for char in chars:
            result+=char*freq[char]
        #RETURN THE FINAL STRING
        return result
s="tree"
obj=Solution()
print(obj.frequencySort(s))