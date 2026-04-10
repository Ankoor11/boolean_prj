from boolean_evaluator import BooleanEvaluator
from truth_table_generator import TruthTableGenerator

def run_demo():
    print("\n" + "="*60)
    print("BOOLEAN EXPRESSION EVALUATOR - DEMO")
    print("="*60 + "\n")
    
    evaluator = BooleanEvaluator()
    truth_gen = TruthTableGenerator(evaluator)
    
    print("EXAMPLE 1: Simple AND Expression")
    print("-" * 60)
    expr1 = "A AND B"
    print(f"Expression: {expr1}\n")
    table1 = truth_gen.generate(expr1)
    print(truth_gen.display(table1))
    
    print("\n" + "="*60)
    print("EXAMPLE 2: Simple OR Expression")
    print("-" * 60)
    expr2 = "A OR B"
    print(f"Expression: {expr2}\n")
    table2 = truth_gen.generate(expr2)
    print(truth_gen.display(table2))
    
    print("\n" + "="*60)
    print("EXAMPLE 3: Complex Expression")
    print("-" * 60)
    expr3 = "(A OR B) AND NOT C"
    print(f"Expression: {expr3}\n")
    table3 = truth_gen.generate(expr3)
    print(truth_gen.display(table3))
    
    print("\n" + "="*60)
    print("EXAMPLE 4: Step-by-Step Evaluation")
    print("-" * 60)
    expr4 = "(A AND B) OR NOT C"
    values = {'A': True, 'B': False, 'C': True}
    print(f"Expression: {expr4}")
    print(f"Variable Values: {values}\n")
    steps = evaluator.get_step_by_step(expr4, values)
    for step in steps:
        print(step)
    
    print("\n" + "="*60)
    print("EXAMPLE 5: Complex Expression with More Variables")
    print("-" * 60)
    expr5 = "(A AND B) OR (C AND NOT D)"
    print(f"Expression: {expr5}\n")
    table5 = truth_gen.generate(expr5)
    print(truth_gen.display(table5))

if __name__ == "__main__":
    run_demo()
