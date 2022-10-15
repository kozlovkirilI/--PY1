money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05


# TODO Оформить решение
def months_left(money_capital, salary, spend, increase):
    month = 0
    while money_capital + salary - spend >= 0:
        money_capital += salary - spend
        spend *= 1 + increase
        month += 1

    return month


month = months_left(money_capital, salary, spend, increase)
print(month)
