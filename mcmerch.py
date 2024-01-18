import sys

# Parse arguments
def parseArguments():
    arguments = {
        "price": float(sys.argv[1]),
        "quantity": 1,
        "province": "ON"
    }
    return arguments

def taxRate(province):
    tax = {
        "ON": 0.13
    }
    return tax[province]

def mcmerchCalculator():
    arguments = parseArguments()
    tax = taxRate(arguments["province"])
    print(round(arguments["price"] * arguments["quantity"] * (1 + tax), 2))

mcmerchCalculator()

