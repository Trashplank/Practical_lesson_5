#Импорты
import random

#Создание словаря?
country = ["Россия", "Австрия", "Азербайджан", "Албания", "Алжир"]
city = ["Москва", "Вена", "Баку", "Тирана", "Алжир"]
good = 0
bad = 0
keychain = {}
for i in range(len(country)):
    keychain[country[i]] = city[i]

print("Викторина! Ура!!!")
#Игра
for i in range(len(country)):
    random_country = random.choice(country)
    print("Какая столица в стране " + random_country + "?")
    input_unit = input("Столица: ")
    if input_unit == keychain[random_country]:
        
        print("Правильно!")
        good += 1
    else:
        print("Ошибка!")
        bad += 1
    num = 0
    for i in country:
        if i == random_country:
            del country[num]
        num += 1
    

print("Правильных: " + str(good))
print("Ошибок: " + str(bad))
    


