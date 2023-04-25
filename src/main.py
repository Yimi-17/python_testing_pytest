#Funcion suma
def sum(x, y):
    return x + y

#Funcion si es mayor al otro valor
def is_greater_than(number_1, number_2):
    return number_1 > number_2


def login(username, password):
    if ((username == "yimicr") and (password == "123456")):
        return True
    else:
        return False