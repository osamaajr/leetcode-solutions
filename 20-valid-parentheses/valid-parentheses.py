class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)

            elif c == ')' or c == ']' or c == '}':
                if not stack:
                    return False 

                top = stack.pop()

                if c == ')' and top != '(': # if you want to close, but the last push (top) isnt an opening, return False
                    return False
                if c == ']' and top != '[':
                    return False
                if c == '}' and top != '{':
                    return False

        return len(stack) == 0
