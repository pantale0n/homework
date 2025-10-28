input_eda = input("Сколько вы потратили на еду? ")
eda = float(input_eda)

input_transport = input("Сколько вы потратили на транспорт? ")
transport = float(input_transport)

input_joy = input("Сколько вы потратили на развлечения? ")
joy = float(input_joy)

summa_trat = eda + transport + joy
srednee = summa_trat / 3

print(f"Общая сумма ваших трат {summa_trat}")
print(f"Среднее значение {srednee}")
