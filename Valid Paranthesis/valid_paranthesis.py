class Solution:
    def isValid(self, s: str) -> bool:
        start = ['{','[','(']
        stack = []
        for val in s:
            if val in start:
                stack.append(val)
            elif stack==[]: return False
            elif((val==')' and stack.pop()!='(') or (val=='}' and stack.pop()!='{')
                or (val==']' and stack.pop()!='[')):
                return False
        return stack==[]
                