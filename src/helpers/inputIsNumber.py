def inputIsNumber(msg):
    numberOfDishes = input(msg)
    if not numberOfDishes.isdigit():
        raise TypeError("Error, Debio ingresar un numero entero")
    return int(numberOfDishes)