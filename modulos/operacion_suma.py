def op_suma(a, b):
    return a + b

def op_resta(a, b):
    return a - b

def op_multiplicacion(a, b):
    return a * b

def op_division(a, b):
    if b == 0:
        return "Error: División por cero no permitida."
    return a / b