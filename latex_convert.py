import re
import matplotlib.pyplot as plt

def convert_to_latex(expr):
    latexed_expr = r''
    coefficient_regex = re.compile(r'^[\-|\+]')
    exponent_regex = re.compile(r'^[\-|\+]')
    for term in expr:
        if len(term) == 3: # Terms with coefficient, variable, and exponent
            fractioned_coefficient = term[0].replace('(', '').replace(')', '').split('/')
            fractioned_exponent = term[2].replace('(', '').replace(')', '').split('/')
            if len(fractioned_coefficient) == 2: # Formatting a fraction coefficient of the term variable
                coefficient_sign = coefficient_regex.findall(fractioned_coefficient[0])
                # print(coefficient_sign)
                if len(coefficient_sign) > 0:
                    latexed_expr += r''+coefficient_sign[0]+r' \frac{'+fractioned_coefficient[0].replace('+', '').replace('-', '')+r'}{'+fractioned_coefficient[1]+r'}'
                else:
                    latexed_expr += r' \frac{'+fractioned_coefficient[0].replace('+', '').replace('-', '')+r'}{'+fractioned_coefficient[1]+r'}'
            elif len(fractioned_coefficient) == 1: # Formatting a non-fraction coefficient of the term variable
                latexed_expr += r' '+fractioned_coefficient[0]
            
            latexed_expr += r' '+term[1]+r'' # Formatting the term variable

            if len(fractioned_exponent) == 2: # Formatting a fraction exponent of the term variable
                exponent_sign = exponent_regex.findall(fractioned_exponent[0])
                if len(exponent_sign) > 0:
                    latexed_expr += r'^{'+exponent_sign[0]+r'\frac{'+fractioned_exponent[0].replace('-', '')+r'}{'+fractioned_exponent[1]+r'}}'
                else:
                    latexed_expr += r'^{\frac{'+fractioned_exponent[0].replace('-', '')+r'}{'+fractioned_exponent[1]+r'}}'
            elif len(fractioned_exponent) == 1: # Formatting a non-fraction exponent of the term variable
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

def latex_to_image(latex_string, image_path):
    fig = plt.figure(figsize=(0.1, 1))

    plt.axis('off')
    plt.text(0.05, 0.05, f'${latex_string}$', fontsize=20)

    plt.savefig(image_path, format='png', bbox_inches='tight', pad_inches=0.05)
    plt.close(fig)