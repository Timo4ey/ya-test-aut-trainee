rocks = ['гора','гора','гора']
items = ['река','гора','небо','гора']


def getMaxRepeadSplit() -> str:
    inp = input("enter something ")
    df = list(filter(None, inp.split(' ')))
    tempDict = {}
    for x in set(df):
        tempDict[x] = df.count(x)
    return max(tempDict, key=tempDict.get)




if __name__ == '__main__':
    # print(getMaxRepead(rocks)) # гора
    # print(getMaxRepead(items)) # гора
    print(getMaxRepeadSplit())



# def main(callback) -> str:
#     tempDict = {}
#     for x in set(df):
#         tempDict[x] = df.count(x)
#     return max(tempDict, key=tempDict.get)