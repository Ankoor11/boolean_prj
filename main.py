from boolean_evaluator import BooleanEvaluator
from truth_table_generator import TruthTableGenerator
from input_validator import *

def main():
    print("\n" + "="*60)
    print("BOOLEAN EXPRESSION EVALUATOR")
    print("="*60)
    print("\nSupported operators: AND, OR, NOT")
    print("Valid variables: A-Z (uppercase letters)")
    print("Example: (A AND B) OR NOT C\n")
    
    evaluator = BooleanEvaluator()
    truth_gen = TruthTableGenerator(evaluator)
    
    while True:
        expression = input("Enter Boolean expression (or 'quit' to exit): ").strip()
        
        if expression.lower() == 'quit':
            print("Thank you for using Boolean Expression Evaluator!")
            break
        
        if not expression:
            print("Error: Empty expression. Please try again.\n")
            continue
        
        is_valid, error_msg = evaluator.validate_expression(expression)
        if not is_valid:
            print(f"Error: {error_msg}\n")
            continue
        
        truth_table = truth_gen.generate(expression)
        print(f"\nTruth Table for: {expression}\n")
        print(truth_gen.display(truth_table))
        
        step_by_step = input("\nShow step-by-step evaluation? (y/n): ").lower()
        if step_by_step == 'y':
            variables = truth_table['variables']
            var_values = {}
            for var in variables:
                val = input(f"Enter value for {var} (T/F): ").upper()
                var_values[var] = (val == 'T')
            steps = evaluator.get_step_by_step(expression, var_values)
            print("\nEvaluation Steps:")
            for step in steps:
                print(step)
        
        print()

if __name__ == "__main__":
    main()
