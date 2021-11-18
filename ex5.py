def glas(text):
    num = 0
    for i in text:
        if (i == "а") or (i =="у") or (i =="е") or (i =="ы") or (i =="о") or (i =="э") or (i =="ё") or (i =="я") or (i =="и") or (i =="ю"):
            num += 1
    return num

def soglas(text):
    num = 0
    for i in text:
        if (i != "а") or (i != "у") or (i != "е") or (i != "ы") or (i != "о") or (i != "э") or (i != "ё") or (i != "я") or (i != "и") or (i != "ю"):
            if i != " ":
                num += 1
    return num

input_unit = str(input("Текст: "))
input_choice = str(input("s/g - согласная/гласная: "))

if input_choice == "s":
    print(soglas(text = input_unit))
elif input_choice == "g":
    print(glas(text = input_unit))
else:
    print("Ошибка")
