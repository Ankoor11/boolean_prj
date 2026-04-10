Boolean Expression Evaluator
============================

A comprehensive Python tool for evaluating Boolean expressions and generating truth tables. This project provides an interactive command-line interface to parse, validate, and evaluate Boolean logic formulas.

Features
--------
*   Expression Parser: Understands standard Boolean logic.
*   Operators Supported: AND, OR, NOT.
*   Variables Supported: Uppercase letters (A-Z).
*   Truth Table Generation: Automatically generates and displays formatting truth tables for any provided expression.
*   Step-by-Step Evaluation: Explains the evaluation process of the expression for specific variable values.
*   Input Validation: Robustly checks for empty, invalid, or malformed expressions.

File Structure
--------------
*   main.py: The main entry point featuring an interactive command-line prompt.
*   boolean_evaluator.py: Contains the core logic for parsing and evaluating expressions step-by-step.
*   truth_table_generator.py: Creates Truth tables from boolean expressions and formats the output.
*   input_validator.py: Contains sanitization and rules for parsing the input strings.
*   demo.py: Provides programmatic examples of the evaluator in action.
*   requirements.txt: Lists any required external dependencies (if applicable).

Usage Instructions
------------------
1. Ensure you have Python installed on your system.
2. If there are external dependencies, install them using:
   pip install -r requirements.txt
3. Run the main interface from your terminal:
   python main.py
4. Follow the on-screen prompts to:
   - Enter a Boolean expression (e.g., "(A AND B) OR NOT C").
   - View its generated truth table.
   - Or display a step-by-step evaluation for explicit True/False (T/F) parameters.

Interactive Console Example
---------------------------
Enter Boolean expression (or 'quit' to exit): A AND B OR NOT C

Truth Table for: A AND B OR NOT C

 A | B | C || Result
---|---|---||--------
 F | F | F || T
 F | F | T || F
 F | T | F || T
 F | T | T || F
 T | F | F || T
 T | F | T || F
 T | T | F || T
 T | T | T || T

Show step-by-step evaluation? (y/n): y
Enter value for A (T/F): T
Enter value for B (T/F): F
Enter value for C (T/F): F

Evaluation Steps:
... [Step by step resolution here]
