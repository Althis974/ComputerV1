#!/usr/bin/env python3

import sys
from parser import *

if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage()
        exit()

    expr = sys.argv[1]
    if not expr:
        usage()
        exit()

    expression, equation, lhs, rhs = parse(expr)

    members = get_members(lhs, rhs)

    degree, a, b, c = get_terms(members)

    display(expr, a, b, c, degree)

    if degree == 1:
        solve_linear(a, b)

    if degree == 2:
        solve_quadratic(a, b, c)
