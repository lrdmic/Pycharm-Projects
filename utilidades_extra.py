import random

metros_en_km = 1000
super_heros = ["Thor", "IronMan", "Hulk", "Wolverine", "Spiderman"]


def tomar_extension(filename):
    return filename[filename.index(".") + 1]


def tirar_dado(num):
    return random.randint(1, num)


