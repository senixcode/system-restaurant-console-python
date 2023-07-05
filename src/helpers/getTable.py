def getTable(dishes):
    result = []
    for dishe in dishes:
        result.append([dishe["id"], dishe["name"], dishe["price"]])
    return result 