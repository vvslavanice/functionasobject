def numberscalculation(y):
    return y + 5

def secondcalculation(z):
    def whatistheresult(y):
        return z(y)
    return whatistheresult

result = secondcalculation(numberscalculation)
print(result(17))
