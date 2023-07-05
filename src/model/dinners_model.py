from helpers.getTable import getTable
from helpers.getResultByDishe import getResultByDishe
# Cena
class Dinners(): 
    __dishes = [
            {"id": 1, "name": "Pasta Alfredo", "price": 18.00},
            {"id": 2, "name": "Lasagña", "price": 19.00},          
        ]
    
    def getDishes(self):
        return getTable(self.__dishes)
    
    def getByIdDishe(self, id):
        print("id")
        for dishe in self.__dishes:
            print("dishe[id]",dishe["id"])
            if dishe["id"] == id:
                return getResultByDishe("Cena", dishe)
        return "No elegio una opción correcta"
                
    
