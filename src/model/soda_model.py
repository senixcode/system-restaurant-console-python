from helpers.getTable import getTable
from helpers.getResultByDishe import getResultByDishe

# Bebidas
class Soda(): 
    __dishes = [
            {"id": 1, "name": "Cafe Personal", "price": 5.00},
            {"id": 2, "name": "Limonada Personal", "price": 6.00},          
        ]
    
    def getDishes(self):
        return getTable(self.__dishes)
    
    def getByIdDishe(self, id):
        for dishe in self.__dishes:
            if dishe["id"] == id:
                return getResultByDishe("Bebida", dishe)
        return "No elegio una opción correcta"