from model.menu_model import Menu
from helpers.inputIsNumber import inputIsNumber

def isContinue():
    table = [["1", "Si"], ["2", "No"]]
    head = ["Numero de Option", "opción"]
    print(Menu().getTable(table, head))
    return inputIsNumber("¿Desea continuar? :")

def main():
     # Intentos
    try:
        numberOfDishes = inputIsNumber("Cuantas platos pedira: ")
        attempts = 1
        report = []
        total = 0.00

        while attempts <= numberOfDishes:
            getDishe = Menu().getByOptionDishes()
            # getDishe = "\n".join("{0} {1}".format(k, v)  for k,v in getDishe.items())
            if not getDishe:
                raise TypeError("Error, Algo salio mal al escoger el plato")
            
            disheOption = getDishe["disheOption"]
            price = getDishe["price"]
            report.append(disheOption)
            total += price

            if attempts == (numberOfDishes ): break

            attempts += 1

            continuing = isContinue()
            if continuing == 1:continue    
            elif continuing == 2: break
        
        return {
            "report": report,
            "total": total
        }
    except ZeroDivisionError:
        return ZeroDivisionError



print(main())