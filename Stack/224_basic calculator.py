class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        current_res = 0
        num = 0
        sign = 1  # 1 for '+', -1 for '-'
        
        for char in s:
            if char.isdigit():
                # Build the number (handles multi-digit numbers)
                num = num * 10 + int(char)
            elif char in "+-":
                # Add the completed number to the result before changing sign
                current_res += sign * num
                num = 0
                sign = 1 if char == '+' else -1
            elif char == '(':
                # Push the result and sign before the parenthesis onto the stack
                stack.append(current_res)
                stack.append(sign)
                # Reset for the new expression inside the parenthesis
                current_res = 0
                sign = 1
            elif char == ')':
                # Finalise the last number inside the parenthesis
                current_res += sign * num
                num = 0
                # Multiply by the sign before the '('
                current_res *= stack.pop()
                # Add to the result before the '('
                current_res += stack.pop()
                
        return current_res + (sign * num)
