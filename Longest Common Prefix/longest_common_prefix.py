class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ""
        for words in zip(*strs):
            if(len(set(words))) > 1:
                return output
            else:
                output += words[0]
                
        return output
            