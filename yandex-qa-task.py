
def getWordMaxRepeadInput() -> str:
    """При запуске функции срабатывает функция input. После ввода создаётся лист. 
    Применена функция фильтр, чтобы не трекать лишние пробелы за слова"""
    inp = input("enter something: ")
    tempList = list(filter(None, inp.split()))
    tempDict = {}
    if len(tempList) < 2:
        return tempList
    for x in set(tempList):
        tempDict[x] = tempList.count(x)
    return max(tempDict, key=tempDict.get)




if __name__ == '__main__':
    # Данные для теста
    # ввод: гора гора гора; вывод: гора
    # ввод: река гора небо гора; вывод: гора 
    print(getWordMaxRepeadInput()) 


