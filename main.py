from source_data import MENU
from source_data import resources


# ===Základní nastavení===
espresso_price = MENU["espresso"]["cost"]
latte_price = MENU["latte"]["cost"]
cappuccino_price = MENU["cappuccino"]["cost"]


# ===funkce===
def report(data):
    print(f"Voda: {data['water']}")
    print(f"Mléko: {data['milk']}")
    print(f"Káva: {data['coffee']}")

def coins():
    print("Prosím vložte mince 1, 2, 5, 10, 20, 50")
    kc1 = int(input("Kolik 1 Kč chcete vložit?: ")) * 1
    kc2 = int(input("Kolik 2 Kč chcete vložit?: ")) * 2
    kc5 = int(input("Kolik 5 Kč chcete vložit?: ")) * 5
    kc10 = int(input("Kolik 10 Kč chcete vložit?: ")) * 10
    kc20 = int(input("Kolik 20 Kč chcete vložit?: ")) * 20
    kc50 = int(input("Kolik 50 Kč chcete vložit?: ")) * 50
    suma = kc1 + kc2 + kc5 + kc10 + kc20 + kc50
    print(f"Celkem jste vložili {suma} Kč")
    return suma

def calculate_change(user_sum_coins, price):
    refund = user_sum_coins - price
    if refund >= 0:
        print("Nápoj se připravuje")
        if refund > 0:
            print(f"Zde jsou peníze zpět: {refund} Kč")
    else:
        print(f"Nevhodili jste dostatek penět. Ještě je zapotřebí vložit {price - user_sum_coins} Kč")

def fill_in_ingredients():
    return resources

def consumption_ingredients(name_of_drink, ingredience): 
    ingredience["water"] = ingredience["water"] - MENU[name_of_drink]["ingredients"]["water"]
    ingredience["milk"] = ingredience["milk"] - MENU[name_of_drink]["ingredients"]["milk"]
    ingredience["coffee"] = ingredience["coffee"] - MENU[name_of_drink]["ingredients"]["coffee"]
    print(f"Zbylé ingrediece : {ingredience}")
    
def calculate_ingredients(drink_name):
    if drink_name == "espresso":
        consumption_ingredients(drink_name, rest_of_ingredients)
    elif drink_name == "latte":
        consumption_ingredients(drink_name, rest_of_ingredients)
    elif drink_name == "cappuccino":
        consumption_ingredients(drink_name, rest_of_ingredients)

def ingredients_checker(in_water, in_milk, in_coffee):
    if in_water < 0:
        print("Nemáme dostatek ingrediencí na tento nápoj")
        exit()
    elif in_milk < 0:
        print("Nemáme dostatek ingrediencí na tento nápoj")
        exit()
    elif in_coffee < 0:
        print("Nemáme dostatek ingrediencí na tento nápoj")
        exit()
    else:
        print("Na váš nápoj máme dostatek ingrediencí")
        return True


# ===Kód automatu===
# Načítáme původní množství ingrediencí
rest_of_ingredients = fill_in_ingredients()


while True:
    # Volba uživatele - jaký chce nápoj
    user_choice = input("Co by jste si dali? (espresso/latte/cappuccino): ")

    # Vypočítá kolik zbývá ingrediencí
    calculate_ingredients(user_choice)

    # Kontrola zda máme dostatek ingrediencí
    if user_choice != "report":
        ingredients_checker(rest_of_ingredients["water"], rest_of_ingredients["milk"], rest_of_ingredients["coffee"])

    # Kontrolní report
    if user_choice == "report":
        report(rest_of_ingredients)

    # Hlavní kód automatu
    if user_choice == "espresso":
        sum = coins()
        print(f"Cena espressa je: {espresso_price} Kč")
        calculate_change(sum, espresso_price)
    elif user_choice == "latte":
        sum = coins()
        print(f"Cena latte je: {latte_price} Kč")
        calculate_change(sum, latte_price)
    elif user_choice == "cappuccino":
        sum = coins()
        print(f"Cena cappuccina je: {cappuccino_price} Kč")
        calculate_change(sum, cappuccino_price)

