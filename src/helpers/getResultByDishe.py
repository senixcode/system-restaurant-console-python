from helpers.msgTypeMenu import msgTypeMenu


def getResultByDishe(type, dishe):
    disheOption = msgTypeMenu(type, dishe)
    return {"disheOption": disheOption, "name": dishe["name"], "price": dishe["price"]}
