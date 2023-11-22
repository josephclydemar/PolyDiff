import fraction_simplify

def differentiate(expr):
    derivative = []
    for term in expr:
        before_diff = ''
        after_diff = ''
        try:
            coefficient = float(fraction_simplify.evaluate(term[0])) * float(term[2])
            exponent = float(term[2]) - 1
            before_diff = f'{term[0]}*{term[1]}^{term[2]}'
            after_diff = f'{coefficient}*{term[1]}^{exponent}'
            derivative.append(after_diff)
            print(term, ' : ', after_diff)
        except IndexError:
            if len(term) > 1:
                before_diff = f'{term[0]}*{term[1]}'
                after_diff = term[0]
                derivative.append(f'{after_diff}')
                print(term, ' : ', after_diff)
            else:
                before_diff = term[0]
                after_diff = '0'
                derivative.append(after_diff)
                print(term, ' : ', after_diff)
    return derivative

