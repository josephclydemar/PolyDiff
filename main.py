import re

expression_search_pattern = r'([0-9]+|x)([\*|\/]x)?(\^[0-9]+)?'
expression_search_regex = re.compile(expression_search_pattern)

term_coefficient_search_pattern = r'(^[0-9]+)'
term_coefficient_search_regex = re.compile(term_coefficient_search_pattern)

term_variable_search_pattern = r'x((\^[0-9]+)$)?'
term_variable_search_regex = re.compile(term_variable_search_pattern)

polynomial_input = input('Enter expression: ')
terms = expression_search_regex.finditer(polynomial_input)

print(terms)

for m in terms:
    # print(m)
    temp = []
    for i in term_coefficient_search_regex.finditer(m.group()):
        temp.append(i.group())
    for i in term_variable_search_regex.finditer(m.group()):
        temp.append(i.group())
    print(temp)