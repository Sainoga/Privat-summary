
print("Приветствую тебя!")


single = int(input("Введи количество синглов: "))
single_price1 = int(input("Цена синглов первый день: "))
single_price2 = int(input("Цена синглов второй день: "))
single_price3 = int(input("Цена синглов третий день: "))
duble = int(input("Количество даблов: "))
duble_price1 = int(input("Цена даблов первый день: "))
duble_price2 = int(input("Цена даблов второй день: "))
duble_price3 = int(input("Цена даблов третий день: "))
excurtions = int(input('Количество тел на экскурсию: '))
excurtions_price = int(input('Цена экскурсии: '))
bus_price = int(input('Цена автобуса: '))


summ_living = (single_price1 + single_price2 + single_price3)  * single + (duble_price2 + duble_price1 + duble_price3) * duble + excurtions_price * excurtions + bus_price


print(f"Общая сумма: {summ_living}")