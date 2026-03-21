def compound_interest(p, r, t):
    amount = p * (pow((1 + r / 100), t))
    return amount