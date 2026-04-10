# ============================================
# BOOLEAN EXPRESSION EVALUATOR
# Python Template Structure
# ============================================
# This file shows the structure and organization
# Copy each section into separate .py files

# FILE 1: boolean_evaluator.py
# ============================================

"""
Core Boolean Expression Evaluator Module

This module contains the main logic for:
- Validating Boolean expressions
- Tokenizing expressions
- Evaluating expressions with given variable values
- Extracting unique variables from expressions
"""

import re
from typing import List, Set, Dict, Tuple


class BooleanEvaluator:
    """Main class for evaluating Boolean expressions"""
    
    def __init__(self):
        """Initialize evaluator with supported operators"""
        self.operators = {'AND', 'OR', 'NOT'}
        self.valid_chars = set('()ABCDEFGHIJKLMNOPQRSTUVWXYZ ')
    
    def validate_expression(self, expression: str) -> Tuple[bool, str]:
        """
        Validate if expression is syntactically correct
        
        Args:
            expression: String containing Boolean expression
            e.g., "(A AND B) OR NOT C"
        
        Returns:
            Tuple[bool, str]: (is_valid, error_message)
            
        Checks:
            1. Contains only valid characters
            2. Parentheses are balanced
            3. Operators are correctly placed
            4. Variables are single uppercase letters
        """
        # TODO: Implement validation logic
        # Step 1: Check for invalid characters
        # Step 2: Check for balanced parentheses
        # Step 3: Check for valid operator syntax
        pass
    
    def tokenize(self, expression: str) -> List[str]:
        """
        Convert expression string to list of tokens
        
        Args:
            expression: String containing Boolean expression
            Example: "(A AND B) OR NOT C"
        
        Returns:
            List[str]: List of tokens
            Example: ['(', 'A', 'AND', 'B', ')', 'OR', 'NOT', 'C']
            
        Implementation Note:
            - Remove extra spaces
            - Keep parentheses as separate tokens
            - Keep operators (AND, OR, NOT) as tokens
            - Keep variables as single tokens
        """
        # TODO: Implement tokenization
        # Step 1: Remove extra spaces
        # Step 2: Identify AND, OR, NOT keywords
        # Step 3: Break into tokens respecting operators
        pass
    
    def get_variables(self, expression: str) -> Set[str]:
        """
        Extract unique variable names from expression
        
        Args:
            expression: String containing Boolean expression
        
        Returns:
            Set[str]: Set of unique variable names
            Example: {'A', 'B', 'C'}
            
        Implementation Note:
            - Extract only uppercase letters A-Z
            - Exclude keywords like AND, OR, NOT
            - Return as set (no duplicates)
        """
        # TODO: Implement variable extraction
        # Use regex or iterate through tokens
        # Return set of variables
        pass
    
    def _apply_not(self, token: str) -> bool:
        """Apply NOT operation to a single boolean value"""
        # TODO: Simple NOT operation
        pass
    
    def _apply_and(self, left: bool, right: bool) -> bool:
        """Apply AND operation to two boolean values"""
        # TODO: Simple AND operation
        pass
    
    def _apply_or(self, left: bool, right: bool) -> bool:
        """Apply OR operation to two boolean values"""
        # TODO: Simple OR operation
        pass
    
    def evaluate(self, expression: str, variable_values: Dict[str, bool]) -> bool:
        """
        Evaluate Boolean expression with given variable values
        
        Args:
            expression: String containing Boolean expression
            Example: "(A AND B) OR NOT C"
            variable_values: Dictionary mapping variables to boolean values
            Example: {'A': True, 'B': False, 'C': True}
        
        Returns:
            bool: Result of evaluation
            
        Algorithm:
            1. Validate input
            2. Tokenize expression
            3. Evaluate respecting operator precedence:
               - Parentheses (highest)
               - NOT
               - AND
               - OR (lowest)
            4. Return boolean result
            
        Example:
            expr = "(A OR B) AND NOT C"
            values = {'A': True, 'B': False, 'C': True}
            result = evaluator.evaluate(expr, values)
            # result = (True OR False) AND NOT True
            # result = True AND False
            # result = False
        """
        # TODO: Implement evaluation logic
        # This is the core function - needs careful implementation
        # Consider using:
        # - Shunting-yard algorithm
        # - Recursive descent parsing
        # - Or simple string substitution with eval (not recommended)
        pass
    
    def get_step_by_step(self, expression: str, variable_values: Dict[str, bool]) -> List[str]:
        """
        Get step-by-step evaluation process
        
        Args:
            expression: Boolean expression
            variable_values: Variable assignments
        
        Returns:
            List[str]: List of evaluation steps
            
        Example Output:
            [
                "Expression: (A OR B) AND NOT C",
                "Values: A=True, B=False, C=True",
                "Step 1: A OR B = True OR False = True",
                "Step 2: NOT C = NOT True = False",
                "Step 3: True AND False = False",
                "Final Result: False"
            ]
        """
        # TODO: Implement step-by-step tracking
        steps = []
        # Add validation
        # Show substitutions
        # Show each operation
        # Show final result
        return steps


# FILE 2: truth_table_generator.py
# ============================================

"""
Truth Table Generator Module

This module handles:
- Generating all combinations of variable values
- Creating truth tables
- Formatting and displaying tables
"""

import itertools
from typing import List, Dict, Any
from boolean_evaluator import BooleanEvaluator


class TruthTableGenerator:
    """Class for generating and displaying truth tables"""
    
    def __init__(self, evaluator: BooleanEvaluator):
        """
        Initialize with evaluator instance
        
        Args:
            evaluator: Instance of BooleanEvaluator
        """
        self.evaluator = evaluator
    
    def generate(self, expression: str) -> Dict[str, Any]:
        """
        Generate complete truth table for expression
        
        Args:
            expression: Boolean expression
            Example: "A AND B"
        
        Returns:
            Dict containing:
            {
                'variables': ['A', 'B'],
                'rows': [
                    {'A': True, 'B': True, 'result': True},
                    {'A': True, 'B': False, 'result': False},
                    ...
                ]
            }
            
        Algorithm:
            1. Extract variables from expression
            2. Generate all 2^n combinations using itertools.product
            3. Evaluate expression for each combination
            4. Store results
            5. Return formatted table
            
        Notes:
            - Number of rows = 2^(number of variables)
            - 2 variables = 4 rows
            - 3 variables = 8 rows
            - 4 variables = 16 rows
        """
        # TODO: Implement truth table generation
        # Step 1: Get unique variables
        variables = self.evaluator.get_variables(expression)
        variables_list = sorted(list(variables))
        
        # Step 2: Generate all combinations
        # Use itertools.product to generate all 2^n combinations
        # Example: for 2 variables: (T,T), (T,F), (F,T), (F,F)
        
        # Step 3: Evaluate for each combination
        rows = []
        # For each combination:
        #   Create dict of variable values
        #   Evaluate expression
        #   Store result
        
        # Step 4: Return formatted table
        result = {
            'variables': variables_list,
            'rows': rows
        }
        return result
    
    def display(self, truth_table: Dict[str, Any]) -> str:
        """
        Display truth table in formatted way
        
        Args:
            truth_table: Truth table dictionary from generate()
        
        Returns:
            str: Formatted table string
            
        Output Format:
            A | B | Result
            --|---|--------
            T | T | T
            T | F | F
            F | T | F
            F | F | F
        """
        # TODO: Implement table formatting
        # Create header with variable names and "Result"
        # Add separator line
        # Add data rows with | separators
        # Return formatted string
        pass
    
    def export_to_csv(self, truth_table: Dict[str, Any], filename: str) -> None:
        """
        Export truth table to CSV file
        
        Args:
            truth_table: Truth table dictionary
            filename: Output CSV filename
        """
        # TODO: Implement CSV export
        pass
    
    def get_statistics(self, truth_table: Dict[str, Any]) -> Dict[str, int]:
        """
        Get statistics about truth table
        
        Args:
            truth_table: Truth table dictionary
        
        Returns:
            Dict with:
            {
                'num_variables': 3,
                'num_rows': 8,
                'num_true': 4,
                'num_false': 4
            }
        """
        # TODO: Implement statistics
        pass


# FILE 3: input_validator.py
# ============================================

"""
Input Validation Module

This module provides utility functions for input validation
"""

import re


def is_balanced_parentheses(expression: str) -> bool:
    """
    Check if parentheses are balanced
    
    Args:
        expression: String to check
    
    Returns:
        bool: True if balanced, False otherwise
        
    Examples:
        is_balanced_parentheses("(A AND B)") → True
        is_balanced_parentheses("((A OR B)") → False
        is_balanced_parentheses("(A AND (B OR C))") → True
    """
    # TODO: Implement parentheses checking
    # Use a counter: +1 for '(', -1 for ')'
    # Never go negative
    # End at 0
    pass


def has_valid_operators(expression: str) -> bool:
    """
    Check if expression contains only valid operators
    
    Args:
        expression: String to check
    
    Returns:
        bool: True if all operators are valid
    """
    # TODO: Check for AND, OR, NOT operators
    # Check that operators are correctly placed
    pass


def has_valid_variables(expression: str) -> bool:
    """
    Check if expression contains only valid variable names
    
    Args:
        expression: String to check
    
    Returns:
        bool: True if all variables are uppercase letters A-Z
    """
    # TODO: Extract all letters and check they're A-Z
    pass


# FILE 4: demo.py
# ============================================

"""
Demo File - Shows Project in Action

Run this file to see examples of the Boolean Expression Evaluator
"""

from boolean_evaluator import BooleanEvaluator
from truth_table_generator import TruthTableGenerator


def run_demo():
    """Run demonstration examples"""
    
    print("\n" + "="*60)
    print("BOOLEAN EXPRESSION EVALUATOR - DEMO")
    print("="*60 + "\n")
    
    # Initialize evaluator
    evaluator = BooleanEvaluator()
    truth_gen = TruthTableGenerator(evaluator)
    
    # ============================================
    # Example 1: Simple AND
    # ============================================
    print("EXAMPLE 1: Simple AND Expression")
    print("-" * 60)
    
    expr1 = "A AND B"
    print(f"Expression: {expr1}\n")
    
    # TODO: Generate and display truth table
    # table1 = truth_gen.generate(expr1)
    # print(truth_gen.display(table1))
    
    # ============================================
    # Example 2: Simple OR
    # ============================================
    print("\n" + "="*60)
    print("EXAMPLE 2: Simple OR Expression")
    print("-" * 60)
    
    expr2 = "A OR B"
    print(f"Expression: {expr2}\n")
    
    # TODO: Generate and display truth table
    
    # ============================================
    # Example 3: Complex with AND, OR, NOT
    # ============================================
    print("\n" + "="*60)
    print("EXAMPLE 3: Complex Expression")
    print("-" * 60)
    
    expr3 = "(A OR B) AND NOT C"
    print(f"Expression: {expr3}\n")
    
    # TODO: Generate and display truth table
    
    # ============================================
    # Example 4: Step-by-Step Evaluation
    # ============================================
    print("\n" + "="*60)
    print("EXAMPLE 4: Step-by-Step Evaluation")
    print("-" * 60)
    
    expr4 = "(A AND B) OR NOT C"
    values = {'A': True, 'B': False, 'C': True}
    
    print(f"Expression: {expr4}")
    print(f"Variable Values: {values}\n")
    
    # TODO: Get and display step-by-step evaluation
    # steps = evaluator.get_step_by_step(expr4, values)
    # for step in steps:
    #     print(step)
    
    # ============================================
    # Example 5: Complex Expression
    # ============================================
    print("\n" + "="*60)
    print("EXAMPLE 5: Complex Expression with More Variables")
    print("-" * 60)
    
    expr5 = "(A AND B) OR (C AND NOT D)"
    print(f"Expression: {expr5}\n")
    
    # TODO: Generate and display truth table


if __name__ == "__main__":
    run_demo()


# FILE 5: main.py
# ============================================

"""
Main Entry Point for Boolean Expression Evaluator

This is the main program that:
1. Gets user input
2. Validates expression
3. Generates truth table
4. Displays results
"""

from boolean_evaluator import BooleanEvaluator
from truth_table_generator import TruthTableGenerator
from input_validator import *


def main():
    """Main program execution"""
    
    print("\n" + "="*60)
    print("BOOLEAN EXPRESSION EVALUATOR")
    print("="*60)
    print("\nSupported operators: AND, OR, NOT")
    print("Valid variables: A-Z (uppercase letters)")
    print("Example: (A AND B) OR NOT C\n")
    
    # Initialize
    evaluator = BooleanEvaluator()
    truth_gen = TruthTableGenerator(evaluator)
    
    while True:
        # Get input
        expression = input("Enter Boolean expression (or 'quit' to exit): ").strip()
        
        if expression.lower() == 'quit':
            print("Thank you for using Boolean Expression Evaluator!")
            break
        
        if not expression:
            print("Error: Empty expression. Please try again.\n")
            continue
        
        # TODO: Validate expression
        # is_valid, error_msg = evaluator.validate_expression(expression)
        # if not is_valid:
        #     print(f"Error: {error_msg}\n")
        #     continue
        
        # TODO: Generate truth table
        # truth_table = truth_gen.generate(expression)
        
        # TODO: Display truth table
        # print(f"\nTruth Table for: {expression}\n")
        # print(truth_gen.display(truth_table))
        
        # TODO: Ask if user wants step-by-step for specific values
        # step_by_step = input("\nShow step-by-step evaluation? (y/n): ").lower()
        # if step_by_step == 'y':
        #     # TODO: Get variable values
        #     # TODO: Show step-by-step
        #     pass
        
        print()


if __name__ == "__main__":
    main()


# FILE 6: requirements.txt
# ============================================

# Optional dependencies (one per line)

# For better table formatting (optional)
# pandas>=1.0.0
# tabulate>=0.8.7

# For testing (optional)
# pytest>=6.0.0

# For code quality (optional)
# pylint>=2.7.0
# black>=21.0.0


# ============================================
# HOW TO USE THIS TEMPLATE
# ============================================

"""
SETUP INSTRUCTIONS:

1. Create a project folder:
   mkdir BooleanExpressionEvaluator
   cd BooleanExpressionEvaluator

2. Create these Python files in the folder:
   - main.py
   - boolean_evaluator.py
   - truth_table_generator.py
   - input_validator.py
   - demo.py
   - requirements.txt

3. Copy the relevant sections from this file into each .py file

4. Start with main.py or demo.py and implement the TODO sections

5. Test each function as you complete it

6. Run demo.py to test:
   python demo.py

7. Run the main program:
   python main.py

IMPLEMENTATION ORDER:

Week 1:
  1. Study the theory (see Complete Guide)
  2. Implement validate_expression() - input validation
  3. Implement tokenize() - expression parsing
  4. Implement get_variables() - variable extraction

Week 2:
  1. Implement evaluate() - core evaluation logic
  2. Test thoroughly with many cases
  3. Implement get_step_by_step() - for transparency

Week 3:
  1. Implement generate() - truth table creation
  2. Implement display() - formatting output
  3. Create demo.py examples

Week 4:
  1. Integrate main.py
  2. Create documentation
  3. Final testing and bug fixes

KEY IMPLEMENTATION TIPS:

1. For validate_expression():
   - Use a counter for parentheses balance
   - Check valid characters with regex
   - Verify operator syntax

2. For tokenize():
   - Split by spaces first
   - Recognize AND, OR, NOT keywords
   - Keep parentheses separate

3. For evaluate():
   - This is the hardest part!
   - Consider using shunting-yard algorithm
   - OR use recursive descent parsing
   - Test with many complex expressions

4. For truth_table_generator():
   - Use itertools.product for combinations
   - Use 2^n to verify row count
   - Format nicely for display

TESTING:

Test each function independently:
  - Valid expressions: "(A AND B)", "A OR B", "NOT A"
  - Complex: "(A OR B) AND NOT C"
  - Edge cases: "((A))", "A AND B AND C"
  - Invalid: "(A AND B", "A && B"
"""
