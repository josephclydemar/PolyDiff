import expr_simplify

def differentiate(expr):
    derivative = []
    for term in expr:
        # before_diff = ''
        after_diff = ''
        if len(term) == 3:
            coefficient = expr_simplify.evaluate(term[0]) * expr_simplify.evaluate(term[2])
            exponent = expr_simplify.evaluate(term[2]) - 1
            # before_diff = f'{term[0]}*{term[1]}^{term[2]}'
            after_diff = f'{coefficient}*{term[1]}^{exponent}'
            derivative.append(after_diff)
            print(term, ' : ', after_diff)
        elif len(term) == 2:
            # before_diff = f'{term[0]}*{term[1]}'
            after_diff = term[0]
            derivative.append(f'{after_diff}')
            print(term, ' : ', after_diff)
        elif len(term) == 1:
            # before_diff = term[0]
            after_diff = '0'
            derivative.append(after_diff)
            # print(term, ' : ', after_diff)
    return derivative

