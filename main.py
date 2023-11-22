import re

expression_search_pattern = r'([\+|\-])?([0-9]+|x)([\*|\/]x)?(\^[0-9]+)?'
expression_search_regex = re.compile(expression_search_pattern)

term_coefficient_search_pattern = r'(^[\+|\-]?[0-9]*)'
term_coefficient_search_regex = re.compile(term_coefficient_search_pattern)

term_variable_search_pattern = r'x((\^[0-9]+)$)?'
term_variable_search_regex = re.compile(term_variable_search_pattern)

variable_search_pattern = r'^x'
variable_search_regex = re.compile(variable_search_pattern)

exponent_search_pattern = r'\^[0-9]+'
exponent_search_regex = re.compile(exponent_search_pattern)

polynomial_input = input('Enter expression: ')
matched_terms = expression_search_regex.finditer(polynomial_input)

print(matched_terms)

for m in matched_terms:
    # print(m)
    temp = []
    for i in term_coefficient_search_regex.finditer(m.group()):
        x = i.group()
        # print(len(x))
        if len(x) == 0:
            temp.append('+1')
        elif len(x) == 1 and (x == '+' or x == '-'):
            temp.append(f'{x}1')
        else:
            temp.append(x)
    for i in term_variable_search_regex.finditer(m.group()):
        for j in variable_search_regex.finditer(i.group()):
            temp.append(j.group())
        for j in exponent_search_regex.finditer(i.group()):
            temp.append(j.group().replace('^', ''))
        # temp.append(i.group())
    print(temp)