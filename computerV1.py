#!/usr/bin/env python3

from tools import *


def get_members(lhs, rhs):
    members = [[], []]

    for i in range(1, len(lhs), 3):
        tmp = lhs[i]
        members[0].append(float(tmp.replace(" ", "")))
        members[1].append(float(lhs[i + 1]))

    for i in range(1, len(rhs), 3):
        tmp = rhs[i]
        members[0].append(-float(tmp.replace(" ", "")))
        members[1].append(float(rhs[i + 1]))

    i = 0
    while i < len(members[0]):
        if not members[0][i]:
            del members[0][i], members[1][i]
            i -= 1
        i += 1

    boolean = 1
    while boolean:
        boolean, i = 0, 0
        while i < len(members[1]):
            tmp = members[1][i]
            j = 0
            while j < len(members[1]) and 1 < len(members[1]):
                if i != j and tmp == members[1][j]:
                    boolean = 1
                    members[0][i] += members[0][j]
                    del members[0][j], members[1][j]
                    j -= 1
                    if i < len(members[0]) and not members[0][i]:
                        del members[0][i], members[1][i]
                j += 1
            i += 1

    return members


def get_terms(members):
    degree = 0
    for i in range(0, len(members[1])):
        if members[1][i] > degree:
            degree = members[1][i]

    if 0 > degree or degree > 2:
        bad_degree()

    a, b, c = 0, 0, 0
    if degree == 1:
        for i in range(0, len(members[1])):
            if members[1][i] == 1:
                a = members[0][i]

            if members[1][i] == 0:
                b = members[0][i]

    elif degree == 2 or not degree:
        for i in range(0, len(members[1])):
            if members[1][i] == 2:
                a = members[0][i]

            if members[1][i] == 1:
                b = members[0][i]

            if members[1][i] == 0:
                c = members[0][i]

    return degree, a, b, c


def solve_linear(a, b):
    print(colored("\n-------------- SOLUTION ----------------\n", "yellow"))
    print(colored("    -b", "cyan"))
    print("X =", colored("———", "cyan"))
    print(colored("     a", "cyan"))
    print("\n   ", -b)
    print("X = —————")
    print("   ", a)
    print("\nX =", end=" ")
    print_float(-b / a, 1)
    print("")


def discriminant(a, b, c):
    print(colored("\n--------------- DISCRIMINANT ---------------\n", "yellow"))
    delta = b ** 2 - 4 * a * c
    print("Δ =", colored("b² - 4ac", "cyan"))
    print("Δ =", "{}² - 4 × {} × {}".format(b, a, c))
    print("Δ =", colored("{}".format(round(delta, 2)), "green"))

    if delta > 0:
        print(colored("\nThe discriminant is positive,", "green"), end=" ")
        print(colored("then there are two distinct roots.", "green"))
    elif not delta:
        print(colored("\nthe discriminant is zero,", "green"), end=" ")
        print(colored("then there is exactly one real root.", "green"))
    else:
        print(colored("\nThe discriminant is negative,", "green"), end=" ")
        print(colored("then there are two distinct complex roots.", "green"))

    return delta


def solve_quadratic(a, b, c):
    delta = discriminant(a, b, c)
    print(colored("\n---------------- SOLUTIONS -----------------\n", "yellow"))

    if delta > 0:
        root1 = (-b + ft_sqrt(delta)) / (2 * a)
        root2 = (-b - ft_sqrt(delta)) / (2 * a)
        print(colored("        -b + √Δ", "cyan"))
        print("root1 =", colored("———————— ", "cyan"))
        print(colored("           2a", "cyan"))
        print("\n        {} + √{}".format(-b, round(delta, 2)))
        print("root1 = ——————————————")
        print("           2 ×", a)
        print("\nroot1 =", end=" ")
        print_float(root1, 1)

        print(colored("\n\n        -b - √Δ", "cyan"))
        print("root2 =", colored("———————— ", "cyan"))
        print(colored("           2a", "cyan"))
        print("\n        {} - √{}".format(-b, round(delta, 2)))
        print("root2 = ——————————————")
        print("           2 ×", a)
        print("\nroot2 =", end=" ")
        print_float(root2, 1)
        print("")

    elif not delta:
        root = -b / (2 * a)
        print(colored("        -b", "cyan"))
        print("root =", colored("—————", "cyan"))
        print(colored("        2a", "cyan"))
        print("\n          {}".format(-b))
        print("root = ———————————")
        print("        2 × {}".format(a))
        print("\nroot =", end=" ")
        print_float(root, 1)
        print("")

    else:
        root = -b / (2 * a)
        xi = ft_sqrt(-delta) / (2 * a)
        print(colored("         -b       √-Δ", "cyan"))
        print("root1 =", colored("———— + i —————", "cyan"))
        print(colored("         2a       2a", "cyan"))
        print("\n            {}          √{}".format(-b, round(-delta, 2)))
        print("root1 = ————————— + i —————————")
        print("        2 x", a, "     2 x", a)
        print("\nroot1 =", end=" ")
        print_float(root, 1)
        sign(a, 0, 1)
        print_float(xi, 1)
        print(colored("i", "green"))

        print(colored("\n         -b       √-Δ", "cyan"))
        print("root2 =", colored("———— - i —————", "cyan"))
        print(colored("         2a       2a", "cyan"))
        print("\n            {}          √{}".format(-b, round(-delta, 2)))
        print("root2 = ————————— - i —————————")
        print("        2 x", a, "     2 x", a)
        print("\nroot2 =", end=" ")
        print_float(root, 1)
        sign(a, 0, 1)
        print_float(-xi, 1)
        print(colored("i", "green"))
