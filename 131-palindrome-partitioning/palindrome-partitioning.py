class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(text):
            return text==text[::-1]
        n=len(s)
        ans=[]
        def func(idx,path):
            if idx==n:
                ans.append(path[:])
                return
            for end in range(idx,n):
                substring=s[idx:end+1]
                if is_palindrome(substring):
                    path.append(substring)

                    func(end+1,path)
                    path.pop()
        func(0,[])
        return ans