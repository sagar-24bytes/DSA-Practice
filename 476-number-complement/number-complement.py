class Solution:
    def findComplement(self, num: int) -> int:
        res=bin(num)[2:]
        com=""
        for b in res:
            if b=="1":
                com+='0'
            else:
                com+='1'
        return int(com,2)

        