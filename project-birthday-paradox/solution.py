def probability_no_match(num_people):
    prob = 1.0
    for i in range(num_people):
        prob *= (365 - i) / 365
    return prob

# probability someone shares a birthday:
def probability_match(num_people):
    return 1 - probability_no_match(num_people)
