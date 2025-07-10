#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calc
    import sys

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    operator_token_list = ['+', '-', '*', '/']
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operator_token = sys.argv[2]
    if operator_token not in operator_token_list:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    if operator_token == '+':
        result = calc.add(a, b)
    elif operator_token == '-':
        result = calc.sub(a, b)
    elif operator_token == '*':
        result = calc.mul(a, b)
    else:
        result = calc.div(a, b)

    print("{} {} {} = {}".format(a, operator_token, b, result))
    sys.exit(0)
