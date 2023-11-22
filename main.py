import re



def parse_expr(string_expr):
    expression_search_pattern = r'([\+|\-])?([0-9]+|(\([0-9]+\/[0-9]+\)))?([\*|\/]?x)?(\^[0-9]+)?'
    expression_search_regex = re.compile(expression_search_pattern)

    term_coefficient_search_pattern = r'(^[\+|\-]?[0-9]*)'
    term_coefficient_search_regex = re.compile(term_coefficient_search_pattern)

    term_variable_search_pattern = r'x((\^[0-9]+)$)?'
    term_variable_search_regex = re.compile(term_variable_search_pattern)

    variable_search_pattern = r'^x'
    variable_search_regex = re.compile(variable_search_pattern)

    exponent_search_pattern = r'\^[0-9]+'
    exponent_search_regex = re.compile(exponent_search_pattern)

    matched_terms = expression_search_regex.finditer(string_expr)
    parsed_expression = []
    for m in matched_terms:
        print(m)
        if m.group() == '':
            continue
        term = []
        for i in term_coefficient_search_regex.finditer(m.group()):
            x = i.group()
            # print(len(x))
            if len(x) == 0:
                term.append('+1')
            elif len(x) == 1 and (x == '+' or x == '-'):
                term.append(f'{x}1')
            else:
                term.append(x)
        for i in term_variable_search_regex.finditer(m.group()):
            for j in variable_search_regex.finditer(i.group()):
                term.append(j.group())
            for j in exponent_search_regex.finditer(i.group()):
                term.append(j.group().replace('^', ''))
        # print(term)
        parsed_expression.append(term)
    return parsed_expression


expr = input('Enter expression: ')
separated_expr = parse_expr(expr)
print(separated_expr)