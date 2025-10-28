input_cena_tovara = input("Введите цену товара: ")
cena_tovara = float(input_cena_tovara)

input_procent_skidki = input("Введите процент вашей скидки: ")
procent_skidki = float(input_procent_skidki)

raschet_procent_skidki = cena_tovara * procent_skidki / 100
cena_new = cena_tovara - raschet_procent_skidki

print(f"Ваша цена со скидко  {cena_new} руб.")