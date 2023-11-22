def evaluate(frac):
    frac = frac.replace('(', '')
    frac = frac.replace(')', '')
    separated_frac = frac.split('/')
    return float(separated_frac[0]) / float(separated_frac[1])
