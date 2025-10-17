print("Привіт я Brawl")
print("я допоможу вибрати бравлера")

name = input("як тебе звати? ")
print("ок,", name, "слухай")

mode = input("який режим ти граєш більше? (solo / gem / brawlball): ")

if mode == "solo":
    print("тобі підійде Едгар або Леон. треба агресивно грати")
elif mode == "gem":
    print("бери персонажа з хілом типу Поко. важливо триматись разом")
elif mode == "brawlball":
    print("Даріл/Бул. пробивати і не боятись йти в лоб")
else:
    print("бери Дінамайка")

rage = input("ти часто в тільті? (так / ні): ")

if rage == "так":
    print("виидали гру")
else:
    print("виидали гру")

print("папа")