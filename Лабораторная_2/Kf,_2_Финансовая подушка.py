money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 1.03  # Ежемесячный рост цен

months = 0
while money_capital > 0:
    for months in range(months + 1):
        money_capital -= spend - salary
        spend *= increase
        months += 1

print("Количество месяцев, которое можно протянуть без долгов:", months)
