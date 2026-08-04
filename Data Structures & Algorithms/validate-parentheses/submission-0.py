class Solution:
    def isMatch(self, lhs, rhs) -> bool:
        case1 = (lhs == '[' and rhs == ']')
        case2 = (lhs == '(' and rhs == ')')
        case3 = (lhs == '{' and rhs == '}')
        return case1 or case2 or case3

    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if stack:
                top = stack[-1]
                if self.isMatch(top, ch):
                    stack.pop()
                    continue
            stack.append(ch)
        return len(stack) == 0