import re

def is_balanced_parentheses(expression: str) -> bool:
    """
    Check if parentheses are balanced
    """
    count = 0
    for char in expression:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
        if count < 0:
            return False
    return count == 0

def has_valid_operators(expression: str) -> bool:
    """
    Check if expression contains only valid operators
    """
    tokens = [t for t in re.split(r'(\s+|\(|\))', expression) if t.strip()]
    for t in tokens:
        if t not in ['AND', 'OR', 'NOT', '(', ')'] and not (len(t) == 1 and 'A' <= t <= 'Z'):
            return False
    return True

def has_valid_variables(expression: str) -> bool:
    """
    Check if expression contains only valid variable names
    """
    words = re.findall(r'[A-Za-z]+', expression)
    for word in words:
        if word not in {'AND', 'OR', 'NOT'}:
            if not (len(word) == 1 and word.isupper()):
                return False
    return True
