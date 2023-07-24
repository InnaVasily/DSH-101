salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 1.03  # Ежемесячный рост цен

money = 0
i = 0
while i <= months-1:
    money += spend - salary
    spend *= increase
    i += 1

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money))