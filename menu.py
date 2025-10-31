category = str(input("Выберите категорию: напиток, суп, десерт: "))

match category:
    case "напиток": # type: ignore
        tea_cena = 50
        cofe_cena = 110
        sok_cena = 210
        napitok = str(input("Выберите напиток: чай, кофе, сок:"))
        if napitok == "чай":
            print(f"Вы выбрали напиток чай, стоимость заказа {tea_cena}")
        elif napitok == "кофе":
            print(f"Вы выбрали напиток кофе, стоимость заказа {cofe_cena}")
        else:
             print(f"Вы выбрали напиток кофе, стоимость заказа {sok_cena}")
    case "суп": # type: ignore
        borsh_cena = 150
        si_cena = 210
        pure_cena = 180
        sup = str(input("Выберите суп: борщ, щи, суп-пюре:"))
        if sup == "борщ":
            print(f"Вы выбрали борщ, стоимость заказа {borsh_cena}")
        elif sup == "щи":
            print(f"Вы выбрали щи, стоимость заказа {si_cena}")
        else:
            print(f"Вы выбрали суп-пюре, стоимость заказа {pure_cena}")
    case _:
        tort_cena = 500
        icecream_cena = 310
        fruct_cena = 410
        desert = str(input("Выберите десерт: торт, мороженое, фрукты:"))
        if desert == "торт":
            print(f"Вы выбрали торт, стоимость заказа {tort_cena}")
        elif desert == "мороженое":
            print(f"Вы выбрали мороженое, стоимость заказа {icecream_cena}")
        else:
            print(f"Вы выбрали фрукты, стоимость заказа {fruct_cena}")
