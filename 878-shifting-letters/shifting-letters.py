class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[int]
        :rtype: str
        """
        total=0
        res=""
        sum_all=sum(shifts)
        for n in range(len(shifts)):
            k=sum_all-total
            res+=chr((ord(s[n])-ord('a')+k)%26 + ord('a'))
            total+=shifts[n]
        return res
        