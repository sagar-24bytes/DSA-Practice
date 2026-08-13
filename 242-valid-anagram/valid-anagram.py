from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen1=Counter(s)
        seen2=Counter(t)
        return seen1==seen2
        
        
        