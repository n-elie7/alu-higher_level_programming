#!/usr/bin/python3
"""Calculator program that imports functions from calculator_1.py"""

from calculator_1 import add, sub, mul, div
import sys


def main():
    """Main function to handle calculator operations"""
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    
    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])
    
    if operator == '+':
        result = add(a, b)
    elif operator == '-':
        result = sub(a, b)
    elif operator == chr(42):
        result = mul(a, b)
    elif operator == '/':
        result = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, " + chr(42) + " and /")
        sys.exit(1)
    
    print("{} {} {} = {}".format(a, operator, b, result))


if __name__ == "__main__":
    main()
