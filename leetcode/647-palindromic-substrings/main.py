class Solution:
    def countSubstrings(self, s: str) -> int:
        
        palindromes = 0
        
        mid = 0
    
        left = mid
        right = mid
    
        while mid < len(s):
            while left >= 0 and right < len(s):
                if s[left] != s[right]:
                    break
                
                palindromes += 1
                
                left -= 1
                right += 1
                            
            mid += 1
            left = mid
            right = mid
        
        mid = 0
        left = mid
        right = left + 1

        while mid < len(s):
            while left >= 0 and right < len(s):
                if s[left] != s[right]:
                    break
                
                palindromes += 1
                
                left -= 1
                right += 1
                            
            mid += 1
            left = mid
            right = left + 1
        
        return palindromes