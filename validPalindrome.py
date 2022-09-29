# Valid Plaindrome

def validPalindrome(self, s: str) -> bool:
    l, r = 0, len(s) - 1
    s = s.lower()
    
    while l < r:
        while l < r and not s[l].isalNum():
            l += 1
        while r > l and not s[r].isalNum():
            r -= 1
        
        if s[l].lower() != s[r].lower():
            return False
        l, r = l + 1, r - 1
    return True

print(validPalindrome)
