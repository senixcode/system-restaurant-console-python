from tabulate import tabulate
from model.lunch_model import Lunch
from model.breakfast_model import Breakfast
from model.dinners_model import Dinners
from model.soda_model import Soda
from helpers.inputIsNumber import inputIsNumber

class Menu:
    __head = ["Numero Opción", "Nombre", "Precio"]
    __classes = {1: Breakfast, 2: Lunch, 3: Dinners, 4: Soda}

    def getTable(self, table, head):
        return tabulate(table, headers=head, tablefmt="grid")

    def getMenu(self):
        table = [
            ["1", "Desayuno"],
            ["2", "ALmuerzo"],
            ["3", "Cena"],
            ["4", "Bebidas"],
        ]
        head = ["Numero Opción", "Nombre"]
        return self.getTable(table, head)

    def getByOptionDishes(self):
        print(self.getMenu())
        id = inputIsNumber("Escriba un opción numero: ")
        if id:
            getClass = self.__classes[id]()
            options = self.getTable(getClass.getDishes(), self.__head)
            print(options)
            numberOption = inputIsNumber("Escriba un opción numero: ")
            return getClass.getByIdDishe(numberOption)
        else:
            return "No elegio una opción correcta"
