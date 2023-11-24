def evaluate(frac):
    frac = frac.replace('(', '')
    frac = frac.replace(')', '')
    separated_frac = frac.split('/')
    if len(separated_frac) < 2:
        return float(separated_frac[0])
    return float(separated_frac[0]) / float(separated_frac[1])
