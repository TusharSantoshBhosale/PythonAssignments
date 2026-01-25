def ChkPrime(no):
    if no < 2:
        return False
    
    for value in range(2,no):
        if no % value == 0:
            return False
    return True
