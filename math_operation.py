import expr_simplify
import latex_convert

def differentiate(expr):
    derivative = []
    count = 0
    for term in expr:
        # before_diff = ''
        after_diff = ''
        if len(term) == 3:
            coefficient = expr_simplify.simplify(f'{term[0]}*{term[2]}')
            exponent = expr_simplify.simplify(f'{term[2]}-1')
            # before_diff = f'{term[0]}*{term[1]}^{term[2]}'
            if coefficient[1] == '+':
                after_diff = [f'+{coefficient}', term[1], exponent]
            else:
                after_diff = [coefficient, term[1], exponent]
            latex_convert.latex_to_image(latex_convert.convert_to_latex([after_diff]), f'./img/step{count}.png')
            derivative.append(after_diff)
            # print(term, ' : ', after_diff)
        elif len(term) == 2:
            # before_diff = f'{term[0]}*{term[1]}'
            after_diff = [term[0]]
            latex_convert.latex_to_image(latex_convert.convert_to_latex([after_diff]), f'./img/step{count}.png')
            derivative.append(after_diff)
            # print(term, ' : ', after_diff)
        elif len(term) == 1:
            # before_diff = term[0]
            after_diff = ['0']
            latex_convert.latex_to_image(latex_convert.convert_to_latex([after_diff]), f'./img/step{count}.png')
            derivative.append(after_diff)
            # print(term, ' : ', after_diff)
        count += 1
    return derivative

