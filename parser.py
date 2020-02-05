#!/usr/bin/env python3

import re
from computerV1 import *


def format_expr(expr):
    i = 0
    s = ""
    while i < len(expr) - 2:
        if natural_form(expr, i) and expr[i + 1] == " " and expr[i + 2] != "*":
            a = expr[:i + 1]
            b = expr[i + 1:]
            s = ""
            seq = a, " * X^0", b
            expr = s.join(seq)
        i += 1

    if natural_form(expr, len(expr) - 1):
        seq = expr, " * X^0"
        expr = s.join(seq)

    if expr[0] == "X":
        seq = "1 * ", expr
        expr = s.join(seq)

    if expr[len(expr) - 3] == "=" and expr[len(expr) - 1] == "X":
        a = expr[:len(expr) - 1]
        seq = a, "1 * X^1"
        expr = s.join(seq)

    if (expr[len(expr) - 3] == "*" or expr[len(expr) - 3] == "-"
            or expr[len(expr) - 3] == "+") and expr[len(expr) - 1] == "X":
        a = expr[:len(expr) - 1]
        seq = a, "X^1"
        expr = s.join(seq)

    expr = expr.replace("X ", "X^1 yo")

    return expr


def parse(expr):
    check_expression(expr)

    expr = format_expr(expr)

    lhs, rhs = expr.split("=")

    lhs = re.split(r"(-*\s*[.0-9]*)\s\*\sX\^(-*[0-9.]*)", lhs)
    rhs = re.split(r"(-*\s*[.0-9]*)\s\*\sX\^(-*[0-9.]*)", rhs)
    equation = re.split(r"(-*\s*[.0-9]*)\s\*\sX\^(-*[0-9.]*)", expr)
    expression = expr

    return expression, equation, lhs, rhs


def check_expression(expr):
    negative_exp = re.findall(r"X\^-", expr)
    if negative_exp:
        bad_degree()

    for i in range(0, len(expr)):
        if expr[i] == 'X' and i + 1 < len(expr) and expr[i + 1] == '^':
            if i + 2 < len(expr) and expr[i + 2].isdigit()\
                    and '0' <= expr[i + 2] <= '2':
                if i + 3 < len(expr)\
                        and (expr[i + 3] == '.' or expr[i + 3].isdigit()):
                    bad_degree()
            elif i + 2 < len(expr) and expr[i + 2].isdigit()\
                    and expr[i + 2] > '2':
                bad_degree()
            elif i + 2 >= len(expr) or not expr[i + 2].isdigit():
                bad_degree()
