import re

def convert_to_latex(expr):
    latexed_expr = r''
    coefficient_regex = re.compile(r'^[\-|\+]')
    for term in expr:
        if len(term) == 3: # Terms with coefficient, variable, and exponent
            fractioned_coefficient = term[0].replace('(', '').replace(')', '').split('/')
            fractioned_exponent = term[2].replace('(', '').replace(')', '').split('/')
            if len(fractioned_coefficient) == 2: # Formatting a fraction coefficient
                coefficient_sign = coefficient_regex.findall(fractioned_coefficient[0])
                print(coefficient_sign)
                latexed_expr += r''+coefficient_sign[0]+r' \frac{'+fractioned_coefficient[0].replace('+', '').replace('-', '')+r'}{'+fractioned_coefficient[1]+r'}'
            elif len(fractioned_coefficient) == 1: # Formatting a non-fraction coefficient
                latexed_expr += r' '+fractioned_coefficient[0]
            
            latexed_expr += r' '+term[1]+r''

            if len(fractioned_exponent) == 2: # Formatting a fraction exponent
                latexed_expr += r'^{\frac{'+fractioned_exponent[0]+r'}{'+fractioned_exponent[1]+r'}}'
            elif len(fractioned_exponent) == 1: # Formatting a non-fraction exponent
                latexed_expr += r'^{'+fractioned_exponent[0]+r'}'

        elif len(term) == 2:
            fractioned_coefficient = term[0].replace('(', '').replace(')', '').split('/')
            if len(fractioned_coefficient) == 2:
                coefficient_sign = coefficient_regex.findall(fractioned_coefficient[0])
                latexed_expr += r''+coefficient_sign[0]+r' \frac{'+fractioned_coefficient[0].replace('+', '').replace('-', '')+r'}{'+fractioned_coefficient[1]+r'}'
            elif len(fractioned_coefficient) == 1:
                latexed_expr += r' '+fractioned_coefficient[0]
            latexed_expr += r' '+term[1]+r''

        elif len(term) == 1:
            fractioned_coefficient = term[0].replace('(', '').replace(')', '').split('/')
            if len(fractioned_coefficient) == 2:
                coefficient_sign = coefficient_regex.findall(fractioned_coefficient[0])
                latexed_expr += r''+coefficient_sign[0]+r' \frac{'+fractioned_coefficient[0].replace('+', '').replace('-', '')+r'}{'+fractioned_coefficient[1]+r'}'
            elif len(fractioned_coefficient) == 1:
                latexed_expr += r' '+fractioned_coefficient[0]
    return latexed_expr

