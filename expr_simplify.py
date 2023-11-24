import sympy as sp

def evaluate(frac):
    frac = frac.replace('(', '')
    frac = frac.replace(')', '')
    separated_frac = frac.split('/')
    if len(separated_frac) < 2:
        return float(separated_frac[0])
    return float(separated_frac[0]) / float(separated_frac[1])

def simplify(expr):
    sympy_expr = sp.simplify(expr)
    string_expr = str(sympy_expr)
    return f'({string_expr})'