class Solution:
    def winnerOfGame(self, s: str) -> bool:
        a = b = 0
        n = len(s)
        for i in range(1,n-1):
            if s[i-1] == s[i] == s[i+1]:
                if s[i] == 'A':
                    a += 1
                else:
                    b += 1
        return a>b