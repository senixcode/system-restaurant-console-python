from helpers.getTable import getTable
from helpers.getResultByDishe import getResultByDishe

# Clase Desayuno
class Breakfast():
    __dishes = [
            {"id": 1, "name": "Hevos al gusto", "price": 6.00},
            {"id": 2, "name": "Omeletter", "price": 6.00},
            {"id": 3, "name": "Het Cake's", "price": 8.00}
        ]
    
    def getDishes(self):
      return getTable(self.__dishes) 
  
    def getByIdDishe(self, id):
        for dishe in self.__dishes:
            print("dishe",dishe)
            if dishe["id"] == id:
                return getResultByDishe("Desayuno", dishe)
        return "No elegio una opción correcta"
       