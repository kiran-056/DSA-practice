class Solution:    
    def anagramStrings(self, s, t):
        t=sorted(t.lower())
        s=sorted(s.lower())
        if s==t:
            return True