#!/usr/bin/env python3

from termcolor import colored


def usage():
    print(colored("Expression is missing.", "red"))


def bad_degree():
    print(colored("Only first and second degree polynomial equation", "red"))
    print(colored("are allowed here.\nGo see there if I'm there!", "red"))
    exit()


def print_float(f, color):
    if color:
        print(colored("{0:.2f}".format(round(f, 2)), "green"), end=" ")
    else:
        print("{0:.2f}".format(round(f, 2)), end=" ")


def ft_sqrt(n):
    a = 1

    for i in range(0, 10):
        a = 0.5 * (a + n / a)

    return a


def natural_form(expression, i):
    if expression[i - 1] != "^" and "0" <= expression[i] <= "9":
        return 1


def sign(a, minus, plus):
    if a >= 0 and plus:
        print(colored("+", "green"), end=" ")
    elif a < 0 and minus:
        print(colored("-", "green"), end=" ")
    elif a <= 0 and plus:
        print(colored("+", "green"), end=" ")


def reduce_form(degree, a, b, c):
    if not degree:
        if not c:
            print(colored(c, "green"), colored("= 0", "green"))
            print(colored("\n---------------- SOLUTION ------------------\n",
                          "yellow"))
            print(colored("|R are solution.", "green"))
        else:
            print(colored(c, "green"), colored("= 0", "green"))
            print(colored("\n---------------- SOLUTION ------------------\n",
                          "yellow"))
            print(colored("Equation without unknowns and insoluble.", "red"))
            print(colored("Nice try huh.", "red"))
        exit()

    if degree == 1:
        if a == 1 or a == -1:
            sign(a, 1, 0)
            print(colored("X", "green"), end=" ")
        else:
            print(colored(a, "green"), colored("* X", "green"), end=" ")

        if b < 0:
            sign(b, 1, 0)
            print(colored(-b, "green"), end=" ")
        elif b > 0:
            sign(b, 0, 1)
            print(colored(b, "green"), end=" ")

        print(colored("= 0", "green"))
        print("\nType:", colored("Linear equation", "cyan"))
        print("Form:", colored("aX + b = 0", "cyan"))

    if degree == 2:
        if a == 1 or a == -1:
            sign(a, 1, 0)
            print(colored("X²", "green"), end=" ")
        else:
            print(colored(a, "green"), colored("* X²", "green"), end=" ")

        if b == 1 or b == -1:
            sign(b, 1, 1)
            print(colored("X", "green"), end=" ")
        elif b:
            sign(b, 0, 1)
            print(colored(b, "green"), colored("X", "green"), end=" ")

        if c:
            sign(c, 0, 1)
            print(colored(c, "green"), end=" ")

        print(colored("= 0", "green"))
        print("\nType:", colored("Quadratic equation", "cyan"))
        print("Form:", colored("aX² + bX + c = 0", "cyan"))


def display(expr, a, b, c, degree):
    print(colored("\n------------------- INPUT ------------------\n", "yellow"))
    print("Original expression:", colored(expr, "green"))

    print(colored("\n--------------- REDUCED FORM ---------------\n", "yellow"))

    print("Reduced form:", end=" ")
    reduce_form(degree, a, b, c)
