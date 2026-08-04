class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        def isOperand(ch: str) -> bool:
            case1 = (ch == '+')
            case4 = (ch == '-')
            case2 = (ch == '*')
            case3 = (ch == '/')

            return case1 or case2 or case3 or case4
        
        def evaluate(operator: str, 
                    lhs: int,
                    rhs: int) -> int:
            match operator:
                case '+':
                    return lhs  + rhs
                case '-':
                    return lhs - rhs
                case '*':
                    return lhs * rhs
                case '/':
                    return int(lhs / rhs)

        for symbol in tokens:
            if isOperand(symbol):
                rhs = stack[-1]
                stack.pop()
                lhs = stack[-1]
                stack.pop()
                value = evaluate(symbol, lhs, rhs)
                stack.append(value)
            else:
                stack.append(int(symbol))
            
        value = stack[-1]
        return value
                