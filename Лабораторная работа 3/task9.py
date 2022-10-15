salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен


# TODO Оформить решение
def need_cash(salary, spend, months, inrease):
    need_money = 0
    for month in range(months):
        need_money += spend - salary
        spend *= 1 + increase

    return need_money


need_money = need_cash(salary, spend, months, increase) # количество денег, чтобы прожить 10 месяцев
print(round(need_money))
