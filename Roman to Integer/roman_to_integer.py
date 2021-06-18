class Solution:
    def romanToInt(self, s: str) -> int:
        symbolDict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        sum = 0
        for i in s:
            sum += symbolDict[i]
        for i in range(1,len(s)):
            if s[i]=="V" or s[i]=="X":
                if s[i-1]=="I":
                    sum -=2
            elif s[i]=="L" or s[i]=="C":
                if s[i-1]=="X":
                    sum -= 20
            elif s[i]=="D" or s[i]=="M":
                if s[i-1]=="C":
                    sum-=200
                    
        return sum
            