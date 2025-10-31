category = str(input("Выберите категорию: напиток, суп, десерт: "))

match category:
    case "Напиток":
        tea_cena = 50
        cofe_cena = 110
        sok_cena = 210
        napitok = str(input("Выберите напиток: чай, кофе, сок:"))
        if napitok == "Чай":
            print(f"Вы выбрали напиток чай, стоимость заказа {tea_cena}")
        elif napitok == "Кофе":
            print(f"Вы выбрали напиток кофе, стоимость заказа {cofe_cena}")
        else:
             print(f"Вы выбрали напиток кофе, стоимость заказа {sok_cena}")
    case "Суп":
        borsh_cena = 150
        si_cena = 210
        pure_cena = 180
        sup = str(input("Выберите суп: борщ, щи, суп-пюре:"))
        if sup == "Борщ":
            print(f"Вы выбрали борщ, стоимость заказа {borsh_cena}")
        elif sup == "Щи":
            print(f"Вы выбрали щи, стоимость заказа {si_cena}")
        else:
            print(f"Вы выбрали суп-пюре, стоимость заказа {pure_cena}")
    case _:
        tort_cena = 500
        icecream_cena = 310
        fruct_cena = 410
        desert = str(input("Выберите десерт: торт, мороженое, фрукты:"))
        if desert == "Борщ":
            print(f"Вы выбрали борщ, стоимость заказа {tort_cena}")
        elif desert == "Щи":
            print(f"Вы выбрали щи, стоимость заказа {icecream_cena}")
        else:
            print(f"Вы выбрали суп-пюре, стоимость заказа {fruct_cena}")
