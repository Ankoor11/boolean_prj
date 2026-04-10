import itertools
from typing import List, Dict, Any
from boolean_evaluator import BooleanEvaluator

class TruthTableGenerator:
    def __init__(self, evaluator: BooleanEvaluator):
        self.evaluator = evaluator
    
    def generate(self, expression: str) -> Dict[str, Any]:
        variables = sorted(list(self.evaluator.get_variables(expression)))
        rows = []
        
        is_valid, _ = self.evaluator.validate_expression(expression)
        if not is_valid:
            return {'variables': [], 'rows': []}

        combinations = itertools.product([True, False], repeat=len(variables))
        for combo in combinations:
            var_dict = dict(zip(variables, combo))
            try:
                res = self.evaluator.evaluate(expression, var_dict)
                row = var_dict.copy()
                row['result'] = res
                rows.append(row)
            except ValueError:
                pass
                
        return {'variables': variables, 'rows': rows}
    
    def display(self, truth_table: Dict[str, Any]) -> str:
        if not truth_table.get('variables'):
            return "Empty or Invalid Table"
            
        variables = truth_table['variables']
        header = " | ".join(variables) + " | Result"
        separator = "-" * len(header)
        
        lines = [header, separator]
        for row in truth_table['rows']:
            row_vals = []
            for var in variables:
                val_str = "T" if row[var] else "F"
                row_vals.append(val_str.center(len(var)))
            res_str = "T" if row['result'] else "F"
            line = " | ".join(row_vals) + f" | {res_str.center(6)}"
            lines.append(line)
        return "\n".join(lines)
    
    def export_to_csv(self, truth_table: Dict[str, Any], filename: str) -> None:
        import csv
        if not truth_table.get('variables'):
            return
            
        variables = truth_table['variables']
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(variables + ['Result'])
            for row in truth_table['rows']:
                writer.writerow([row[var] for var in variables] + [row['result']])
                
    def get_statistics(self, truth_table: Dict[str, Any]) -> Dict[str, int]:
        if not truth_table.get('variables'):
            return {}
            
        rows = truth_table['rows']
        num_true = sum(1 for r in rows if r['result'])
        return {
            'num_variables': len(truth_table['variables']),
            'num_rows': len(rows),
            'num_true': num_true,
            'num_false': len(rows) - num_true
        }
