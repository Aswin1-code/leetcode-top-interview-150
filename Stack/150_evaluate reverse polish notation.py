class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            if token not in {"+", "-", "*", "/"}:
                # If it's a number, push to stack
                stack.append(int(token))
            else:
                # Pop the two most recent operands
                # Note: b is the second operand, a is the first
                b = stack.pop()
                a = stack.pop()
                
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    # Truncate toward zero (Python's // floors toward -inf)
                    # int(a / b) handles truncation correctly for positive/negative
                    stack.append(int(a / b))
                    
        return stack[0]
