#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    operators = ['+', '-', '*', '/']
    op = sys.argv[2]
    if op not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        if op == "+":
            res = add(a, b)
            print(f"{a} {op} {b} = {res}")
        if op == "-":
            print(f"{a} {op} {b} = {sub(a, b)}")
        if op == "*":
            print(f"{a} {op} {b} = {mul(a, b)}")
        if op == "/":
            print(f"{a} {op} {b} = {div(a, b)}")
