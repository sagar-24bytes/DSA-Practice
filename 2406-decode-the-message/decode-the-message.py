class Solution(object):
    def decodeMessage(self, key, message):
        """
        :type key: str
        :type message: str
        :rtype: str
        """
        code={}
        x=0
        for m in range(len(key)):
            if key[m].islower() and key[m] not in code:
                code[key[m]]=chr(ord('a')+x)
                x+=1
                if x==26:
                    break
        ans=""
        for m in message:
            if m.islower():
                ans+=code[m]
            else:
                ans+=m
        return ans
            

        