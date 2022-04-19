def getkey():
    with open("botKey.key", "r") as f:
        text = f.read()
        return text