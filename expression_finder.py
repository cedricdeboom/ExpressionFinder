"""
Expression Finder
Generate all possible equations using +, -, *, /, (, and ), given a list of numbers and an outcome.
"""

from __future__ import division
import itertools

OPERATORS = ['+', '-', '*', '/']
PARENTHESES = ['(', ')', '']

TINY = 1E-10

def tree_search(input=(1,3,4,6), expression="", d=0, e=3, res=24):
    expression_new = expression + str(input[d])
    if d == e:
        bracketing(open=e+1, close=0, n_brackets=0, d=0, e=e+1, expression=expression_new, res=res)
    else:
        for i in xrange(len(OPERATORS)):
            tree_search(input, expression_new + OPERATORS[i], d+1, e, res)

def bracketing(open, close, n_brackets, d=0, e=3, expression="", res=24):
    if d == e:
        expression_new = expression
        for i in xrange(close):
            expression_new += ')'
        o = 0
        c = 0
        for ex in expression_new:
            if ex == PARENTHESES[0]:
                o += 1
            if ex == PARENTHESES[1]:
                c += 1
            if c > o:
                return
        evaluate(expression_new, res)
    else:
        for i in xrange(len(PARENTHESES)):
            if i == 0:
                bracketing(open-1, close+1, n_brackets+1, d+1, e, expression[0:2*d+n_brackets] + "(" + expression[2*d+n_brackets:len(expression)], res)
            elif i == 1:
                bracketing(open, close-1, n_brackets+1, d+1, e, expression[0:2*d+1+n_brackets] + ")" + expression[2*d+1+n_brackets:len(expression)], res)
            else:
                bracketing(open, close, n_brackets, d+1, e, expression, res)


def evaluate(expression, res):
    try:
        if abs(eval(expression) - res) <= TINY:
            print expression + " = " + str(res)
    except:
        pass


if __name__ == '__main__':
    ## CHANGE PARAMS HERE
    numbers = [34, 10, 0]
    res = 34.0
    ##
    c = itertools.permutations(numbers, len(numbers))
    for n in c:
        tree_search(n, "", 0, len(numbers)-1, res)