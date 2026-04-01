<<<<<<< HEAD

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        path=[]
        result=[]
        def backtrack(start):
            if start==len(s):
                result.append(path[:])
                return
            for end in range(start,len(s)):
                sub=s[start:end+1]
                if sub==sub[::-1]:
                    path.append(sub)
                    backtrack(end+1)
                    path.pop()
        backtrack(0)
        return result
=======
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        path=[]
        result=[]
        def backtrack(start):
            if start==len(s):
                result.append(path[:])
                return
            for end in range(start,len(s)):
                sub=s[start:end+1]
                if sub==sub[::-1]:
                    path.append(sub)
                    backtrack(end+1)
                    path.pop()
        backtrack(0)
        return result
        
>>>>>>> 36188a59f7055e72bf63e6f4f5de02b1735df4bd
