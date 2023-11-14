""" TODO: Enter docstring for module main"""

import argparse
import math
import re

def create_interval(min, max, size):
    if(size==0):
        raise ValueError("Size must be > 0")
    if(min > max):
        raise ValueError("min must be smaller or equal to max")
    delta = (max - min) / (size-1)
    return [min + i * delta for i in range(size)]

def validate_func_ops(func: str):
    pattern = re.compile(r'[0-9x+*/%-]')
    if re.search(pattern, func) is None:
        raise ValueError("Only [0-9x+*/%-] are allowed!")
    return True
    

def validate_func_vals(func: str, values: list):
    valid = True
    for x in values:
        try:
            # Beschraenkung der globals aus Sicherheitsgründen
            y = eval(func, {"math": math, "x": x})
        except Exception:
            valid = False
            raise ZeroDivisionError("Division by 0 not allowed!")
    return valid

def calc_vals(func: str, values: list):
    try:
        validate_func_vals(func, values)
    except ZeroDivisionError:
        return []
    finally:
        if(validate_func_ops(func) == False):
            return []
    return [eval(func, {"math": math, "x": x}) for x in values]

def create_table(func: str, min: int, max: int, size: int):
    print(f'f(x) = {func}')
    print('------------------------------')
    print('step'.center(8, ' '), '|', 'x'.center(8, ' '), '|', 'y'.center(8, ' '))
    print('------------------------------')

    interval = (max - min) / (size - 1)

    for i in range(size):
        x = min + i * interval
        y = eval(func.replace('x', str(x)))
        print(f'{i}'.center(8, ' '), '|', f'{x:.2f}'.center(8, ' '), '|', f'{y:.2f}'.center(8, ' '))

def calc():
    parser = argparse.ArgumentParser(description="funcPlot")
    parser.add_argument("expression", type=str, help="Funktionsgleichung, z.B. '2*math.sin(x)+1'")
    parser.add_argument("x_min", type=float, help="Untere Intervallgrenze")
    parser.add_argument("x_max", type=float, help="Obere Intervallgrenze")
    parser.add_argument("steps", type=int, help="Wie viel Schritte")
    args = parser.parse_args()

    create_table(args.expression, args.x_min, args.x_max, args.steps)



if __name__ == "__main__":
    calc()