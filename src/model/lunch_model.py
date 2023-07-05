from helpers.getTable import getTable
from helpers.getResultByDishe import getResultByDishe

# ALmuerzo            
class Lunch():
    __dishes = [
            {"id": 1, "name": "Arroz Chaufa", "price": 18.00},
            {"id": 2, "name": "Arroz con Mariscos", "price": 18.00},
            {"id": 3, "name": "Arroz con Pollo", "price": 17.00},
        ]
    
    def getDishes(self):
        return getTable(self.__dishes)
        
    def getByIdDishe(self, id):
        print("id", id)
        for dishe in self.__dishes:
            print("dishe[id]",dishe["id"])
            if dishe["id"] == id:
                return getResultByDishe("Almuerzo", dishe)
        return "No elegio una opción correcta"
                