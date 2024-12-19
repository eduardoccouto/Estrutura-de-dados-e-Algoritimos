class Solution:
    def reverseWords(self, s: str) -> str:
        l, r = 0, 0
        response = ''
        
        while r < len(s):
            if s[r] != ' ': 
                r += 1
            else:
                response += s[l:r+1][::-1]
                r += 1
                l = r
                
        response += ' '
        response += s[l:r +2][::-1]
        return response[1:]
                
                
a = Solution()
print(a.reverseWords("eduardo couto"))
        
        
        
        
        
        
        