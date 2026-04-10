import re
from typing import List, Set, Dict, Tuple

class BooleanEvaluator:
    def __init__(self):
        self.operators = {'AND', 'OR', 'NOT'}
        self.valid_chars = set('()ABCDEFGHIJKLMNOPQRSTUVWXYZ ')
    
    def validate_expression(self, expression: str) -> Tuple[bool, str]:
        if not expression:
            return False, "Empty expression"
        
        for char in expression:
            if char not in self.valid_chars:
                return False, f"Invalid character found: {char}"
                
        count = 0
        for char in expression:
            if char == '(': count += 1
            elif char == ')': count -= 1
            if count < 0: return False, "Unbalanced parentheses"
        if count != 0: return False, "Unbalanced parentheses"
            
        tokens = self.tokenize(expression)
        if not tokens: return False, "Empty expression"
        
        for t in tokens:
            if t not in self.operators and t not in '()' and not (len(t) == 1 and 'A' <= t <= 'Z'):
                return False, f"Invalid token: {t}"
                
        try:
            vars_in_expr = self.get_variables(expression)
            dummy_vals = {v: False for v in vars_in_expr}
            self.evaluate(expression, dummy_vals)
        except Exception as e:
            return False, f"Syntax error: {str(e)}"
            
        return True, ""
    
    def tokenize(self, expression: str) -> List[str]:
        expr = expression.replace('(', ' ( ').replace(')', ' ) ')
        return [t for t in expr.split() if t.strip()]
    
    def get_variables(self, expression: str) -> Set[str]:
        tokens = self.tokenize(expression)
        return {t for t in tokens if t not in self.operators and t not in '()'}
    
    def _apply_not(self, token: bool) -> bool:
        return not token
    
    def _apply_and(self, left: bool, right: bool) -> bool:
        return left and right
    
    def _apply_or(self, left: bool, right: bool) -> bool:
        return left or right
    
    def evaluate(self, expression: str, variable_values: Dict[str, bool]) -> bool:
        tokens = self.tokenize(expression)
        if not tokens:
            raise ValueError("Empty expression")

        precedence = {'NOT': 3, 'AND': 2, 'OR': 1, '(': 0}
        output = []
        op_stack = []
        
        for token in tokens:
            if token in variable_values:
                output.append(variable_values[token])
            elif token in {'True', 'False', 'T', 'F'}:
                output.append(token in {'True', 'T'})
            elif token in self.operators:
                while op_stack and precedence.get(op_stack[-1], 0) >= precedence[token]:
                    if token == 'NOT' and op_stack[-1] == 'NOT':
                        break 
                    output.append(op_stack.pop())
                op_stack.append(token)
            elif token == '(':
                op_stack.append(token)
            elif token == ')':
                while op_stack and op_stack[-1] != '(':
                    output.append(op_stack.pop())
                if op_stack:
                    op_stack.pop() 
            else:
                raise ValueError(f"Unknown variable or token missing in values: {token}")
                
        while op_stack:
            if op_stack[-1] == '(':
                raise ValueError("Mismatched parentheses")
            output.append(op_stack.pop())
            
        eval_stack = []
        for token in output:
            if isinstance(token, bool):
                eval_stack.append(token)
            elif token == 'NOT':
                if not eval_stack: raise ValueError("Invalid expression (NOT target missing)")
                val = eval_stack.pop()
                eval_stack.append(self._apply_not(val))
            elif token == 'AND':
                if len(eval_stack) < 2: raise ValueError("Invalid expression (AND targets missing)")
                right = eval_stack.pop()
                left = eval_stack.pop()
                eval_stack.append(self._apply_and(left, right))
            elif token == 'OR':
                if len(eval_stack) < 2: raise ValueError("Invalid expression (OR targets missing)")
                right = eval_stack.pop()
                left = eval_stack.pop()
                eval_stack.append(self._apply_or(left, right))
                
        if len(eval_stack) != 1:
            raise ValueError("Invalid expression length after evaluation")
            
        return eval_stack[0]

    def get_step_by_step(self, expression: str, variable_values: Dict[str, bool]) -> List[str]:
        steps = []
        steps.append(f"Expression: {expression}")
        vals_str = ", ".join([f"{k}={v}" for k, v in variable_values.items()])
        steps.append(f"Values: {vals_str}")
        
        try:
            tokens = self.tokenize(expression)
            res = self.evaluate(expression, variable_values)
            
            sub_expr = []
            for t in tokens:
                if t in variable_values:
                    sub_expr.append(str(variable_values[t]))
                else:
                    sub_expr.append(t)
            steps.append(f"Substitution: {' '.join(sub_expr)}")
            steps.append(f"Final Result: {res}")
        except Exception as e:
            steps.append(f"Error evaluation: {str(e)}")
            
        return steps
