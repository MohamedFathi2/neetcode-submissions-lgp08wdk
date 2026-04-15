class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        corresponds = {'(':')', '{':'}', '[':']'}
        for c in s:
            if c in corresponds: # if c is an opening bracket, add it to the stack.
                stack.append(c)
            else:
                if len(stack):
                    top = stack.pop()
                    if corresponds[top] != c:
                        return False
                else:
                    return False
        Valid = not bool(stack)
        return Valid